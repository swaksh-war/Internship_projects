import torch.nn as nn
import torch

class resnet12(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv3t12 = nn.Conv2d(3,12, kernel_size=3, stride=1, padding=1)
        
        self.conv12t48 = nn.Conv2d(12,48, kernel_size=3, stride=1, padding=1)
        
        self.conv48t96 = nn.Conv2d(48,96, kernel_size=3, stride=1, padding=1)
        self.conv96t96a = nn.Conv2d(96,96, kernel_size=3, stride=1, padding=1)
        
        self.conv96t192 = nn.Conv2d(96,192, kernel_size=3, stride=1, padding=1)
        self.conv192t192a = nn.Conv2d(192,192, kernel_size=3, stride=1, padding=1)
        self.conv192t192b = nn.Conv2d(192,192, kernel_size=3, stride=1, padding=1)
        self.conv192t192c = nn.Conv2d(192,192, kernel_size=3, stride=1, padding=1)
        
        self.conv192t384 = nn.Conv2d(192,384,kernel_size=3,stride=1, padding=1)
        self.conv384t384a = nn.Conv2d(384,384, kernel_size=3, stride=1, padding=1)
        self.conv384t384b = nn.Conv2d(384,384, kernel_size=3, stride=1, padding=1)
        self.conv384t384c = nn.Conv2d(384,384, kernel_size=3, stride=1, padding=1)
        
        self.pool = nn.MaxPool2d(2,2)
        
        self.norm12 = nn.BatchNorm2d(12)
        self.norm48 = nn.BatchNorm2d(48)
        self.norm96 = nn.BatchNorm2d(96)
        self.norm192 = nn.BatchNorm2d(192)
        self.norm384 = nn.BatchNorm2d(384)
        
        self.relu = nn.ReLU()
        
        self.adpool = nn.AdaptiveAvgPool2d(1) 
        
        # self.drop = nn.Dropout(0.2)
                                         
        self.linear = nn.Linear(384, 2)
        
        self.flat = nn.Flatten()
        
    
    def forward(self,x):
        out = self.conv3t12(x) # 32x 32  12
        out = self.norm12(out)
        out = self.relu(out)
        out = self.conv12t48(out) # 32 x32  48
        out = self.norm48(out)
        out = self.relu(out)
        out = self.pool(out) #16x16  48
        
        out = self.conv48t96(out)  # 16x 16 96
        out = self.norm96(out)
        y = out
        out = self.relu(out)
        out = self.conv96t96a(out) # 16x 16 96
        out= self.relu(out+y)
        out = self.pool(out) # 8x8 96
        
        out = self.conv96t192(out) # 8x8 192
        out = self.norm192(out)
        y = out
        out = self.relu(out)
        out = self.conv192t192a(out)
        out = self.relu(out+y)
        out = self.conv192t192b(out)
        out = self.relu(out+y)
        out = self.conv192t192c(out)
        out = self.relu(out+y)
        
        out = self.conv192t384(out)
        out = self.norm384(out)
        y = out
        out = self.relu(out)
        out = self.conv384t384a(out)
        out = self.relu(out+y)
        out = self.conv384t384b(out)
        out = self.relu(out+y)
        out = self.conv384t384c(out)
        out = self.relu(out)
        
        
        out = self.adpool(out)
        out = self.flat(out)
        # out = self.drop(out)
        out = self.linear(out)
        out = torch.softmax(out, dim=-1)
        
        return out