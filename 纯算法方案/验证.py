# coding=gbk
# -*- coding:uft-8 -*-
# 验证

from PIL import Image
import os
from number import numberLs


def main():
    countLs = [[], [], [], [], [], [], [], [], []]
    success = 0
    for file in os.listdir('../testset'):
        code = file.split('_')[1].split('.')[0]
        image = Image.open(f'../testset/{file}').resize((40, 19))
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
        lossLs_1, lossLs_2, lossLs_3, lossLs_4 = [], [], [], []
        for numberLi in numberLs:
            loss_1, loss_2, loss_3, loss_4 = 0, 0, 0, 0
            for i in range(190):
                loss_1 += (pixelLs_1[i] - numberLi[i]) ** 2
                loss_2 += (pixelLs_2[i] - numberLi[i]) ** 2
                loss_3 += (pixelLs_3[i] - numberLi[i]) ** 2
                loss_4 += (pixelLs_4[i] - numberLi[i]) ** 2
            lossLs_1.append(loss_1)
            lossLs_2.append(loss_2)
            lossLs_3.append(loss_3)
            lossLs_4.append(loss_4)
        res = ''.join([str(i.index(min(i)) + 1) for i in [lossLs_1, lossLs_2, lossLs_3, lossLs_4]])
        print(code, res)
        if code == res:
            success += 1
        for i in range(4):
            if code[i] == res[i]:
                countLs[int(code[i]) - 1].append(1)
            else:
                countLs[int(code[i]) - 1].append(0)
    for i in range(9):
        print(i + 1, sum(countLs[i]) / len(countLs[i]))
    print(success / len(os.listdir('../testset')) * 100)


if __name__ == '__main__':
    main()
