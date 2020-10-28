# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:29:00 2020

@author: Administrator
"""

import re
import random
num=''
for x in range(10):
    x=random.randint(1000,9999)
    num+='1301111'+str(x)+" "
print(num)
print('以2或4结尾的手机号有',end='')
    
rs=re.findall("\d{10}[^\D24]",num)
print(10-len(rs),'个')
for item in rs:
    print(item,end=' ')