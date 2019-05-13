#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

a = []
with open('test.txt', 'r') as f:
    data = f.readlines()  # txt中所有字符串读入data

    for line in data:
        test = line.split()  # 将单个数据分隔开存好
        a.append(test)
print(a)