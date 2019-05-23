#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import re

the_line = []
constrlist = np.zeros(1787443,dtype=int)
with open('weibo_network.txt', 'r') as f:
    line = f.readlines()
    this_line = line[1]
    p_tmp = [int(i) for i in this_line.split()]
    the_line.append(p_tmp)

    for i in range(2, len(the_line[0]) - 1, 2):

        if the_line[0][i+1] == 0:  # 单方面follow
            constrlist[the_line[0][i]] = 3
        else:
            constrlist[the_line[0][i]] = 2

a = 0
influencefactor0 = np.zeros(1787443,dtype=int)
for i in range(len(constrlist)):
    a += constrlist[i]
for i in range(len(constrlist)):
    if constrlist[i] != 0:
        b = a
        b += constrlist[i]
        influencefactor0[i] = b
print(influencefactor0)
