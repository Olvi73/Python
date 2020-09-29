# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
a=[0]*20
for n in range(20):
    a[n]=random.randint(0,100)
b=[str(i) for i in a]
print("输出前的序列:"+','.join(b))
num1=0
for n in range(20):
    if a[n]%2!=0:
        num1+=1
n=0
num2=20
while n<len(a):
    if a[n]%2!=0:
        del(a[n])
        num2-=1
        continue
    n+=1
b=[str(i) for i in a]
print("输出后的序列:"+','.join(b))
print("一共有:",num1,"个奇数")
print("输出序列有:",num2,"个偶数")

'''
import random
a=[0]*20
for n in range(20):
    a[n]=random.randint(0,100)
b=[str(i) for i in a]
print("输出前的序列:"+','.join(b))
num1=0
for n in range(20):
    if a[n-20]%2!=0:
        del(a[n-20])
        num1+=1
        continue

b=[str(i) for i in a]
print("输出后的序列:"+','.join(b))
print("一共有:",num1,"个奇数")
print("输出序列有:",len(b),"个偶数")
'''