# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 08:43:23 2020

@author: Oliver
"""

n=int(input())
s=0
p=0
if 1<=n<=1000000:
    for i in range(1,n+1):
        if i%9==0:
            for j in str(i):
                s+=int(j)
            if s==9:
                p+=1
            s=0
print(p)