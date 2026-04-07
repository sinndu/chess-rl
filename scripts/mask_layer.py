import torch
import torch.nn
import torch.nn.functional as F

class MaskLayer(nn.Module): # mask layer in nn module that masks 0 and 1s based on legal moves
    def __init__(self):
        super(MaskLayer, self).__init__()

    def forward(self, x, mask):
        return torch.mul(x,mask)