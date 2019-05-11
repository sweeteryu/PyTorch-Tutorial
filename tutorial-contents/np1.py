#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

a = np.loadtxt('weibo_network.txt')[:1]#将test文件作为npy文件读取出来
print(a)
#np.save('test.npy',a)#存储a为npy文件
#test=np.load('test.npy')#读取该npy文件
#print(test)

#with open('odom.txt', 'r') as f:
#    data = f.readlines()  # txt中所有字符串读入data

 #   for line in data:
  #      odom = line.split()  # 将单个数据分隔开存好
   #     numbers_float = map(float, odom)  # 转化为浮点数
    #    print(numbers_float)