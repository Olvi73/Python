# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def f(*a):
    b=[int(n) for n in var.split(' ')]
    rs=[0]*2
    s=0
    for x in range(len(b)):
        s+=b[x]
    rs[0]=min(b)
    rs[1]=s
    return  rs

var=input("请开始输入：")
print("最小值：",f(var)[0],"输入数据之和：",f(var)[1])
    