# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:40:02 2020

@author: Administrator
"""
# import cmath
import math

print("输入方程形如ax^2+bx+c=0")
var=input("请输入方程参数(a b c)：")
a=[float(n) for n in var.split(' ')]
print(a[0],"x^2+",a[1],"x+",a[2],"=0")
def crack(a):
    ans=[0]*2
    dt=(a[1]**2)-(4*a[0]*a[2])
    # if(dt<0):
    #     ans[0]=((-a[1]-cmath.sqrt(dt))/2*a[0])
    #     ans[1]=((-a[1]+cmath.sqrt(dt))/2*a[0])
    # else:
    ans[0]=((-a[1]-math.sqrt(dt))/2*a[0])
    ans[1]=((-a[1]+math.sqrt(dt))/2*a[0])
    return ans
print("x1=",crack(a)[0],"x2=",crack(a)[1])