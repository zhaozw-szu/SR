import torch
import torch.nn as nn
import torch.functional as F

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

class SRCNNA(nn.Module):
    def __init__(self,channels=1):
        super(SRCNNA,self).__init__()
        self.attention_blk = SELayer(64,reduction=4)
        self.conv1 = nn.Conv2d(channels,64,kernel_size=9,padding=9//2)
        self.conv2 = nn.Conv2d(64,128,kernel_size=5,padding=5//2)
        self.conv3 = nn.Conv2d(128,256,kernel_size=5,padding=5//2)
        self.conv4 = nn.Conv2d(256,32,kernel_size=5,padding=5//2)
        self.conv5 = nn.Conv2d(32, channels, kernel_size=5, padding=5 // 2)
        self.relu1 = nn.ReLU(inplace=True)
        self.relu2 = nn.ReLU(inplace=True)
        self.attention_sblk = SpatialAttention()

    def forward(self,x):
        out = self.conv1(x)
        out = self.attention_blk(out)
        out = self.attention_sblk(out)*out
        out = self.relu1(out)
        out = self.conv2(out)
        out = self.relu1(out)
        out = self.conv3(out)
        out = self.relu2(out)
        out = self.conv4(out)
        out = self.relu1(out)
        out = self.conv5(out)
        return out
