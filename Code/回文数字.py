# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:34:55 2020

@author: Oliver
"""

a=[]
n=0
for x in range(100,999):
    s=str(x)
    if s[0]!=s[-1]:continue
    a.append(x)
    n+=1
    if n==10:break
else:
    print('over!')
print(a)


a=[]
n=0
for x in range (0,10000):
    s=str(x)
    if s!=s[::-1]:continue
    a.append(x)
    n+=1
print(a)
print(n)
