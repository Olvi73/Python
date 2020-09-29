# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:57:33 2020

@author: Oliver
"""
num=int(input("输入n："))
x=[ int(i) for i in range(num+1)]
x=x[1::2]
line=int((num+1)/2)
for n in range(line):
    gap=0
    while gap<line-n-1: #递减输出空格
        gap+=1
        print("",end='  ')
    for j in range(x[n]):   #顺序输出切片后的长度
        print("*",end=' ')
    print("")
for n in range(line-1):
    gap=0
    while gap<n+1:  #递增输出空格
        gap+=1
        print("",end='  ')
    for j in range(x[-2-n]):   #顺序输出切片后的长度
        print("*",end=' ')
    print("")
