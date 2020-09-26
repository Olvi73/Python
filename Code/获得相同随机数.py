# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:49:14 2020

@author: Oliver
"""

"""
三位数
mc0
第532914次
time cost 125.17652797698975 s

二位数(5次运行中小于1w次获得相同结果)
hA
第7747次
time cost 1.459421157836914 s

一位数(5次运行结果小于100次)
J
第41次
time cost 0.010970592498779297 s

其中有一次：
随机生成的密码：
6
0
第0次
6
第1次
time cost 0.0 s

"""
import time
import random

low='abcdefghijklmnopqrstuvwxyz'
up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num=0
a=[0]*1
print('随机生成的密码：')
for n in range(1):
    choice=random.randint(1,3)
    if choice==1:
        a[n]=random.randint(0,9)
    elif choice==2:
        a[n]=random.choice(low)
    elif choice==3:
        a[n]=random.choice(up)
b=[str(i) for i in a]
time_start=time.time()
print(''.join(b))
str1=''.join(b)
str2=''
while str2!=str1:
    for n in range(1):
        choice=random.randint(1,3)
        if choice==1:
            a[n]=random.randint(0,9)
        elif choice==2:
            a[n]=random.choice(low)
        elif choice==3:
            a[n]=random.choice(up)
    c=[str(i) for i in a]
    print(''.join(c))
    print("第%d次"%num)
    str2=''.join(c)
    num+=1
time_end=time.time()
print('time cost',time_end-time_start,'s')