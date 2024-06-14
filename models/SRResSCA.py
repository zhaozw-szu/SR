from torch import nn
import torch
import math

class SRResSCA(nn.Module):
    def __init__(self):
        super(SRResSCA,self).__init__()
        self.conv1 = nn.Conv2d(3,64,kernel_size=9,padding=4,padding_mode='reflect',stride=1)
        self.relu = nn.PReLU()
        self.resblk = self._makelayer_(ResBlock,64,64,16)
        self.CAblk = SELayer(64,reduction=4)
        self.SAblk = SpatialAttention()
        self.conv2 = nn.Conv2d(64,64,kernel_size=1,stride=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu2 = nn.PReLU()
        self.convpos1 = nn.Conv2d(64,256,kernel_size=3,stride=1,padding=2,padding_mode='reflect')
        self.pixelshuffler1 = nn.PixelShuffle(2)
        self.relupos1 = nn.PReLU()
        self.convpos2 = nn.Conv2d(64,256,kernel_size=3,stride=1,padding=1,padding_mode='reflect')
        self.pixelshuffler2 = nn.PixelShuffle(2)
        self.relupos2 = nn.PReLU()
        self.conv3 = nn.Conv2d(64,3,kernel_size=9,stride=1)
    
    def _makelayer_(self,block,inchannels,outchannels,blocks):
        layers = []
        layers.append(block(inchannels,outchannels))
        for i in range(blocks):
            layers.append(block(outchannels,outchannels))
        return nn.Sequential(*layers)

    def forward(self,x):
        x = self.conv1(x)
        x = self.relu(x)
        residual = x
        out = self.CAblk(x)
        out = self.resblk(out)
        out = self.conv2(out)
        out = self.bn1(out)
        out += residual
        out = self.SAblk(out)*out
        out = self.convpos1(out)
        out = self.pixelshuffler1(out)
        out = self.relupos1(out)
        out = self.convpos2(out)
        out = self.pixelshuffler2(out)
        out = self.relupos2(out)
        out = self.conv3(out)
        return out
        
    
class ResBlock(nn.Module):

    def __init__(self,inchannels,outchannels):
        super(ResBlock,self).__init__()
        self.conv1 = nn.Conv2d(inchannels,outchannels,kernel_size=1,bias=False)
        self.bn1 = nn.BatchNorm2d(outchannels)
        self.conv2 = nn.Conv2d(outchannels,outchannels,kernel_size=3,stride=1,padding=1,bias=False)
        self.bn2 = nn.BatchNorm2d(outchannels)
        self.relu = nn.PReLU()
    
    def forward(self,x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        out += residual
        out = self.relu(out)
        return out

class SELayer(nn.Module):
    def __init__(self, channel, reduction=4):
        super(SELayer, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction,bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel//reduction,channel,bias=False),
            nn.Sigmoid()
        )
    
    def forward(self,x):
        b, c, _, _ = x.size()
        out = self.avg_pool(x).view(b,c)
        out = self.fc(out).view(b,c,1,1)
        return x* out.expand_as(x)

class SpatialAttention(nn.Module):
    def __init__(self,kernel_size=7):
        super(SpatialAttention, self).__init__()
        assert kernel_size in (3,7)
        padding = 3 if kernel_size == 7 else 1 
        self.conv1 = nn.Conv2d(2,1,kernel_size,padding=padding,bias=False)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self,x):
        avg_out = torch.mean(x,dim=1,keepdim=True)
        max_out,_ = torch.max(x,dim=1,keepdim=True)
        x = torch.cat([avg_out,max_out],dim=1)
        x = self.conv1(x)
        return self.sigmoid(x)