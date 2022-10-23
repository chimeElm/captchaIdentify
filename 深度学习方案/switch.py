# coding=gbk
# -*- coding:uft-8 -*-
# switch

import torch
from codedataset import codeDataset
from torch.utils.data import DataLoader

if __name__ == '__main__':
    test_dataset = codeDataset('testset')
    test_dataloader = DataLoader(test_dataset, batch_size=1, shuffle=True)
    model = torch.load('model.pth').cuda(0)
    for images, labels in test_dataloader:
        images = images.cuda(0)
        input_name = ['input']
        output_name = ['output']
        torch.onnx.export(model, images, 'model.onnx', input_names=input_name, output_names=output_name,
                          verbose=True)
        break
