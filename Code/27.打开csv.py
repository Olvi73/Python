# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:02:36 2020

@author: Administrator
"""

import csv
file=csv.reader(open('1.csv','r'))
data=[]
summary=0
n=0
for line in file:
    print(line[0],end=' ')
    print(line[1],end=' ')
    print(line[2])
    n+=1
    summary+=float(line[1])
    data.append(line[1])
print('平均值：',summary/n)