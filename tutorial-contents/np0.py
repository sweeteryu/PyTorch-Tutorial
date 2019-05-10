#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

#a = []b = []for i in range(6):    a.append(i)for i in range(6):    b.append(a)np.save('test2.npy', b)

#test = np.load('adjacency_matrix.npy')
#print(test.ndim) print(test.shape)

with open('weibo_network.txt') as file_object:
    lines = file_object.readlines()
for line in lines[:5]:
    print(line)