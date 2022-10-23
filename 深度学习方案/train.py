# coding=gbk
# -*- coding:uft-8 -*-
# train

import torch
import time
from tqdm import tqdm
from codedataset import codeDataset
from torch.utils.data import DataLoader
from torch import nn
from torch.optim import Adam
import torchvision.models as models

if __name__ == '__main__':
    train_dataset = codeDataset('dataset')
    train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True, drop_last=True, num_workers=4)
    model = models.resnet18(num_classes=4 * 10).cuda(0)
    loss_fn = nn.MSELoss().cuda(0)
    optim = Adam(model.parameters(), lr=0.001)
    model.train()
    for epoch in range(4):
        now = time.time()
        print(f'训练轮数: {epoch + 1}')
        bar = tqdm(enumerate(train_dataloader), total=len(train_dataloader))
        for i, (images, labels) in bar:
            optim.zero_grad()
            images = images.cuda(0)
            labels = labels.cuda(0)
            outputs = model(images).reshape(32, 4, 10)
            loss = loss_fn(outputs, labels)
            loss.backward()
            optim.step()
            if i % 100 == 0:
                print(f'训练次数: {i}, 损失率: {loss.item()}')
        torch.save(model, f'model{epoch}.pth')
