# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 08:54:48 2020

@author: Oliver
"""

import re
def convert(value,strtype,finaltype):
    size = 1024.000000
    count=0
    units = ["B", "KB", "MB", "GB"]
    for t in units:
        if t==strtype:
            st=count
        if t==finaltype:
            ft=count
        count+=1
    if st>ft:
        for i in range(st-ft):
            value = value * size
        return "%.6f" % (value)
    else:
        for i in range(ft-st):
            value = value / size
        return "%.6f" % (value)
    
s=input("")
value=re.findall(r'\d+',str(s))
strtype=re.search('MB|GB|KB|B',str(s)).group()
finaltype=re.search(r'[?](MB|GB|KB|B)',str(s)).group()[1:]
print(convert(float(value[0]),strtype,finaltype))