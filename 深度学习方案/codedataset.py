# coding=gbk
# -*- coding:uft-8 -*-
# codedataset

import os
from PIL import Image
from torch.utils.data import Dataset
import torch
from torchvision import transforms


class codeDataset(Dataset):
    def __init__(self, root_dir):
        super(codeDataset, self).__init__()
        self.image_path = [os.path.join(root_dir, image_name) for image_name in os.listdir(root_dir)]
        self.transforms = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize([100, 300]),
            # transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # 归一化不便于前端处理数据
        ])

    def __len__(self):
        return self.image_path.__len__()

    def __getitem__(self, index):
        image_path = self.image_path[index]
        image = Image.open(image_path).convert('RGB')
        image = self.transforms(image)
        code_label = image_path.split('/')[-1].split('_')[1].split('.')[0]
        code_label = torch.as_tensor([[eval(i)] for i in code_label], dtype=torch.int64)
        one_hot = torch.zeros(4, 10).long()
        one_hot.scatter_(dim=1, index=code_label.long(), src=torch.ones(4, 10).long())
        one_hot = one_hot.to(torch.float32)
        return image, one_hot


if __name__ == '__main__':
    train_data = codeDataset('dataset')
    print(train_data)
