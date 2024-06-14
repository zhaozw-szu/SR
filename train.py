import argparse
import os
import copy
import torch
from torch import nn
import torch.optim as optim
import torch.backends.cudnn as cudnn
from torch.utils.data.dataloader import DataLoader
from torch.autograd import Variable
from tqdm import tqdm

from models.models import SRCNN, VDSR, SRResNet
from models.LapSRN import Net as LapSRN
from models.CARN import Net as CARN
from models.memnet import MemNet as MemNet
from models.SRGAN import Generator,Discriminator
from models.SRCNNA import SRCNNA
from models.SRResSCA import SRResSCA
from utils import AverageMeter, calc_psnr,GeneratorLoss
import torch.nn.functional as F
from dataset import PreprocessDataset


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-file', type=str, default='dataset/train_data.h5')
    parser.add_argument('--eval-file', type=str, default='dataset/test_data.h5')
    parser.add_argument('--outputs-dir', type=str, default='Result')
    parser.add_argument('--scale', type=int, default=4)
    parser.add_argument('--lr', type=float, default=1e-4)
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--num-epochs', type=int, default=200)
    parser.add_argument('--num-workers', type=int, default=8)
    parser.add_argument('--seed', type=int, default=123)
    args = parser.parse_args()

    args.outputs_dir = os.path.join(args.outputs_dir, 'x{}'.format(args.scale))

    if not os.path.exists(args.outputs_dir):
        os.makedirs(args.outputs_dir)

    cudnn.benchmark = True
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print("Training on ",device)

    torch.manual_seed(args.seed)

    train_dataset = PreprocessDataset()
    train_dataloader = DataLoader(train_dataset, batch_size=args.batch_size)

    eval_dataset = PreprocessDataset('dataset/Set5-test/')
    eval_dataloader = DataLoader(eval_dataset, batch_size=args.batch_size)


    modelName = "SRResSCA"
    needup = False
    modelD = Discriminator().to(device)
    optimizerD = optim.Adam(modelD.parameters(),lr=args.lr)
    
    if modelName == "SRCNN":
        model = SRCNN(3).to(device)
        needup = True
    elif modelName == "SRResNet":
        model = SRResNet().to(device)
    elif modelName == "VDSR":
        model = VDSR().to(device)
        needup = True
    elif modelName == "LapSRN":
        model = LapSRN().to(device)
    elif modelName == "CARN":
        model = CARN().to(device)
        needup = True
    elif modelName == "MemNet":
        model = MemNet(3, 64, 6, 6).to(device)
        needup = True
    elif modelName == "SRGAN":
        model = Generator(args.scale).to(device)
        GANloss = GeneratorLoss().to(device)
        needup = False
    elif modelName == "SRCNNA":
        model = SRCNNA(3).to(device)
        needup = True
    elif modelName == "SRResSCA":
        model = SRResSCA().to(device)

    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=args.lr)

    best_weights = copy.deepcopy(model.state_dict())
    best_epoch = 0
    best_psnr = 0.0

    for epoch in range(args.num_epochs):
        model.train()
        epoch_losses = AverageMeter()
        if(modelName=="SRGAN"):
            modelD.train()
        with tqdm(total=(len(train_dataset) - len(train_dataset) % args.batch_size), ncols=80) as t:
            t.set_description('epoch: {}/{}'.format(epoch, args.num_epochs - 1))

            for data in train_dataloader:
                inputs, labels = data
                inputs = inputs.to(device)
                labels = labels.to(device)
                if needup:
                    inputs = F.interpolate(inputs, size=labels.shape[2:], mode='bicubic', align_corners=False)
                if(modelName=="SRGAN"):
                    g_update_first=True
                    real_img = Variable(labels)
                    z = Variable(inputs)
                    real_img = real_img.to(device)
                    # print(real_img.shape)
                    z = z.to(device)
                    fake_img = model(z)
                    # print(fake_img.shape)
                    modelD.zero_grad()
                    real_out = modelD(real_img).mean()
                    fake_out = modelD(fake_img).mean()
                    d_loss = 1 - real_out + fake_out
                    d_loss.backward(retain_graph=True)
                    optimizerD.step()
                    model.zero_grad()
                    fake_img = model(z)
                    fake_out = modelD(fake_img).mean()
                    g_loss = GANloss(fake_out,fake_img,real_img)
                    g_loss.backward()
                    fake_img = model(z)
                    fake_out = modelD(fake_img).mean()
                    optimizer.step()
                    model.eval()
                    preds = model(inputs)
                    loss = criterion(preds,labels)
                    epoch_losses.update(loss.item(),len(inputs))
                # inputs, labels = data
                # inputs = inputs.to(device)
                # labels = labels.to(device)
                # if needup:
                #     inputs = F.interpolate(inputs, size=labels.shape[2:], mode='bicubic', align_corners=False)
                else:
                    preds = model(inputs)
                    loss = criterion(preds, labels)
                    epoch_losses.update(loss.item(), len(inputs))
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()

                t.set_postfix(loss='{:.6f}'.format(epoch_losses.avg))
                t.update(len(inputs))

        torch.save(model.state_dict(), os.path.join(args.outputs_dir, 'epoch_{}.pth'.format(epoch)))

        model.eval()
        epoch_psnr = AverageMeter()

        for data in eval_dataloader:
            inputs, labels = data

            inputs = inputs.to(device)
            if needup:
                inputs = F.interpolate(inputs, size=labels.shape[2:], mode='bicubic', align_corners=False)

            labels = labels.to(device)

            with torch.no_grad():
                preds = model(inputs).clamp(0.0, 1.0)

            epoch_psnr.update(calc_psnr(preds, labels), len(inputs))

        print('eval psnr: {:.2f}'.format(epoch_psnr.avg))

        if epoch_psnr.avg > best_psnr:
            best_epoch = epoch
            best_psnr = epoch_psnr.avg
            best_weights = copy.deepcopy(model.state_dict())

    print('best epoch: {}, psnr: {:.2f}'.format(best_epoch, best_psnr))
    torch.save(best_weights, os.path.join(args.outputs_dir, 'best.pth'))