from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
import dlib
import pandas as pd
import torchvision.models as models

import sys
sys.path.append('/usr/local/lib/python3.6/dist-packages')

def rect_to_bb(rect):
	# take a bounding predicted by dlib and convert it
	# to the format (x, y, w, h) as we would normally do
	# with OpenCV
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
	# return a tuple of (x, y, w, h)
	return (x, y, w, h)

if __name__ == "__main__":
    #Please create a csv with one column 'img_path', contains the full paths of all images to be analyzed.
    #Also please change working directory to this file.
    dlib.DLIB_USE_CUDA = True
    print("using CUDA?: %s" % dlib.DLIB_USE_CUDA)
    #Run training & validation

    train_paths = pd.read_csv('./fairface_label_train.csv')
    val_paths = pd.read_csv('./fairface_label_val.csv')

    resnet18 = models.resnet18()
    loss_func = nn.MSELoss(reduction='sum')
    learning_rate = 0.0001

    data_loader = torch.utils.data.DataLoader(yesno_data,
                                          batch_size=1,
                                          shuffle=True)

    resnet18()

    print(resnet18)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")