import torch,torchvision
from torchsummary import summary
from models.SRCNNA import SRCNNA
from models.SRResSCA import SRResSCA
from models.models import SRResNet
# 检查维度：
if __name__ == "__main__":
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = SRResSCA()
    # model = SRResNet()
    model = model.to(device)
    summary = summary(model,(3,19,19))