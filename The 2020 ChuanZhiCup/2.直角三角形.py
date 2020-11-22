# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 08:48:16 2020

@author: Oliver
"""

c=int(input(""))
for a in range(1,c):
    if (c**2)-(a**2)>0:
        b=int(((c**2)-float(a**2))**(1/2))
        if a**2+b**2==c**2:
            print(a,b)
            break