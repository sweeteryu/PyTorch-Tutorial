#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

n=5
b=np.zeros([n+1,n+1],dtype=int)
a = np.loadtxt('test.txt')#将test文件作为npy文件读取出来
print(a)
for i in range(0,n):
    b[0][i+1] = b[i+1][0] = a[i][0]
for i in range(n):
    for j in range(len(a[i])):
        b[i+1][]
print(b)