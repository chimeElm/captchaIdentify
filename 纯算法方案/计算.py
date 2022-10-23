# coding=gbk
# -*- coding:uft-8 -*-
# 计算

import numpy as np


def main():
    total = []
    for i in range(9):
        i += 1
        file = f'number/{i}.txt'
        ls = []
        for row in open(file, encoding='utf-8').readlines():
            ls.append(eval(row.strip()))
        mean = [int(i) for i in list(np.mean(np.array(ls), axis=0))]
        total.append(mean)
    print(total)


if __name__ == '__main__':
    main()
