# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:27:31 2020

@author: Oliver
"""

import random

#print("成绩为：",x)

for n in range(10):
    a=0
    b=0
    c=0
    d=0
    e=0
    for n in range(1000):
        x=random.randint(0,100)
        if x>=90:
    #        print("A")
            a+=1
        elif x<90 and x>=80:
    #        print("B")
            b+=1
        elif x<80 and x>=70:
    #        print("C")
            c+=1
        elif x<70 and x>=60:
    #        print("D")
            d+=1
        elif x<60:
    #        print("E")
            e+=1
    print(a,b,c,d,e)