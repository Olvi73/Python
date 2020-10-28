# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:08:21 2020

@author: Oliver
"""

def f(n,x):
    rs=''
    #n为待转换的十进制数，x为机制，取值为2-16
    a=[0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
    b=[]
    while True:
        s=n//x  # 商
        y=n%x  # 余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    for i in b:
        rs+=str(a[i])
    return rs
x=int(input("输入十进制数:"))
print("二进制:0b",f(x,2),sep='')
print("八进制:0o",f(x,8),sep='')
print("十六进制:0x",f(x,16),sep='')