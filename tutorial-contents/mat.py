#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scipy.io as sio
import numpy as np

a = np.zeros([2,2],dtype=int)
sio.savemat('test.mat',{'foo':a})

b0 = 'test.mat'
c0 = sio.loadmat(b0)
#print(c0)

b = 'blogcatalog.mat'
c = sio.loadmat(b)

#print(type(c))
print(c)