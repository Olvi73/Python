# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:03:22 2020

@author: Administrator
"""

import re

myfile=open('def.py',encoding='utf-8')
txt=myfile.read()
list=re.findall('def \w*\(\):',txt)
for item in list:
    print(re.search("\w*\(\)",item).group())