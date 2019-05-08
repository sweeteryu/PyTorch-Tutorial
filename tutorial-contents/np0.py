#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

a = []
b = []
for i in range(6):
    a.append(i)
for i in range(6):
    b.append(a)
np.save('test2.npy', b)

test = np.load('/np/PoTorch-Tutorial/tutorial-contents/test2.npy')
print(test.ndim)
print(test.shape)