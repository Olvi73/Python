# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:51:25 2020

@author: Administrator
"""
import re

myfile=open('Mystr.txt',encoding='utf-8')
txt=myfile.read()
list=re.findall('\d',txt)
newtxt=''
for item in list:
    newtxt+=item
print('原字符串：',txt)
print("获取的数字",newtxt)