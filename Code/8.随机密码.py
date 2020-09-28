 # -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:21:58 2020

@author: Administrator
"""
import random

low='abcdefghijklmnopqrstuvwxyz'
up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a=[0]*8
print('随机生成的密码：')
for n in range(8):
    for n in range(8):
        choice=random.randint(1,3)
        if choice==1:
            a[n]=random.randint(0,9)
        elif choice==2:
            a[n]=random.choice(low)
        elif choice==3:
            a[n]=random.choice(up)
    b=[str(i) for i in a]
    print(''.join(b))



