#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import re

n = int(input('please input center node id n:'))
#生成邻接矩阵
filename = 'weibo_network.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
adjacentmatrix = np.zeros([1787443,1787443],dtype=int)
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
#for i in range(0,1787443):
 #   a[0][i+1] = a[i+1][0] = pos[i+1][0]
for i in range(1,1787444):
    #print(len(pos[i]))
    for j in range(2,len(pos[i])-1,2):
           if j%2 == 0 and j != 0:
               #print(pos[i][j])
               if pos[i][j+1] == 0: #单方面follow
                   #print(pos[i][j])
                   adjacentmatrix[i-1][pos[i][j]] = 1
                   adjacentmatrix[pos[i][j]][i-1] = 0
               #互相follow
               else:
                   adjacentmatrix[i-1][pos[i][j]] = 1
                   adjacentmatrix[pos[i][j]][i-1] = 1
               #print(adjacentmatrix)
#print('the adjacentmatrix is:%s'%adjacentmatrix)

#生成基础关注度
indegree = adjacentmatrix.sum(axis=0)
basicattenlist = indegree
#print('the basicattenlist is:%s'%basicattenlist)

#生成follow结构信息
constrmatrix = np.zeros([1787443,1787443],dtype=int)
for i in range(1787443):
    for j in range(1787443):
        if adjacentmatrix[i][j] == 1:
            if adjacentmatrix[j][i] == 1:
                constrmatrix[i][j] = 2
            else:
                constrmatrix[i][j] = 3
#print('the constrmatrix is:%s'%constrmatrix)
constrlist = constrmatrix[n]
#print('when node id=%d,the constrlist is:%s'%(n,constrlist))

#生成结构信息计算的十进制结果
a = 0
influencefactor0 = []
for i in range(len(constrlist)):
    a += constrlist[i]
for i in range(len(constrlist)):
    b = a
    b += constrlist[i]
    influencefactor0.append(b)
#print('influencefactor0:%s'%influencefactor0)

#叠加基础关注度,并[dropout]生成十进制影响力因子列表
influencefactor=[]
for i in range(len(influencefactor0)):
    if constrlist[i] == 0:
        influencefactor.append(0)
    else:
        influencefactor.append(influencefactor0[i] + basicattenlist[i])
print('the influencefactor list is %s'%influencefactor)