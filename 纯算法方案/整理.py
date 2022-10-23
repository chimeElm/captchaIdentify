# coding=gbk
# -*- coding:uft-8 -*-
# 整理

from PIL import Image
import os


def main():
    for file in os.listdir('../dataset'):
        code = file.split('_')[1].split('.')[0]
        image = Image.open(f'../dataset/{file}').resize((40, 19))
        pixelLs = [i[0] * 0.299 + i[1] * 0.587 + i[2] * 0.114 for i in image.getdata()]
        pixelLs = [255 if i > 150 else 0 for i in pixelLs]
        pixelLs_1, pixelLs_2, pixelLs_3, pixelLs_4 = [], [], [], []
        for i in range(760):
            if 2 <= i % 40 < 12:
                pixelLs_1.append(pixelLs[i])
            if 11 <= i % 40 < 21:
                pixelLs_2.append(pixelLs[i])
            if 20 <= i % 40 < 30:
                pixelLs_3.append(pixelLs[i])
            if 29 <= i % 40 < 39:
                pixelLs_4.append(pixelLs[i])
        open(f'number/{code[0]}.txt', 'a', encoding='utf-8').write(str(pixelLs_1) + '\n')
        open(f'number/{code[1]}.txt', 'a', encoding='utf-8').write(str(pixelLs_2) + '\n')
        open(f'number/{code[2]}.txt', 'a', encoding='utf-8').write(str(pixelLs_3) + '\n')
        open(f'number/{code[3]}.txt', 'a', encoding='utf-8').write(str(pixelLs_4) + '\n')
        print(file)


if __name__ == '__main__':
    main()
