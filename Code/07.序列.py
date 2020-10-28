# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:02:31 2020

@author: Administrator
"""

var=input("输入一个序列:")
a=[int(n) for n in var.split(' ')]
lenth=len(a)
max=a[0]
min=a[0]
sum=0
for num in range(lenth):
    sum+=a[num]
    if a[num]>=max:
        max=a[num]
    if a[num]<=min:
        min=a[num]
print("最大值为：",max)
print("最小值为：",min)
avg=(sum-max-min)/(lenth-2)
print("平均值为：%.2f"%avg)





