# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:46:51 2020

@author: Oliver
"""

n=int(input("请输入整数n:"))
def count(n):
    a,b=1,2
    for _ in range(n):
        a,b=b,a+b
    return a
def run(sum,n):
    assert n>0,"n>0" #表达式为假时抛出AssertionError错误
    if n<=1:
        return count(1)+sum
    sum+=count(n)/count(n-1)
    return run(sum,n-1)
sum=0
rs=run(sum,n)
print("S的值为；%.3f"%rs)