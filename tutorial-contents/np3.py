#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

filename = 'test.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
a = np.zeros([6,6],dtype=int)
pos = []
with open(filename, 'r') as f:
  while True:
    lines = f.readline() # 整行读取数据
    if not lines:
      break
      pass
    p_tmp = [int(i) for i in lines.split()] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
    pos.append(p_tmp)  # 添加新读取的数据
    pass
  pos = np.array(pos) # 将数据从list类型转换为array类型。
  pass
for i in range(0,5):
    a[0][i+1] = a[i+1][0] = pos[i+1][0]
for i in range(1,6):
    #print(len(pos[i]))
    for j in range(2,len(pos[i])-1,2):
           if j%2 == 0 and j != 0:
               #print(pos[i][j])
               if pos[i][j+1] == 0: #单方面follow
                   #print(pos[i][j])
                   a[i][pos[i][j]+1] = 1
                   a[pos[i][j]+1][i] = 0
               #互相follow
               else:
                   a[i][pos[i][j] + 1] = 1
                   a[pos[i][j] + 1][i] = 1
print(a)
