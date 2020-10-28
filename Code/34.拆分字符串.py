# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import re

oldstr="Doing is better than saying"
list=re.findall(r"\w[^\s]*",oldstr)
newstr=''
for item in list:
    newstr+=item
print('初始字符串：',oldstr)
print('插分后的字符串：',newstr)