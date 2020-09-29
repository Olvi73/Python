# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:22:51 2020

@author: Oliver
"""

x={'1':'one','2':'two','3':'three','name':'python','tool':'markdown'}
key=input("输入键:")

try:
    print(x[key])
except:
    print("您输入的键不存在！")
    
# value=input('输入值:')
# print(list(x.keys())[list(x.values()).index(value)])