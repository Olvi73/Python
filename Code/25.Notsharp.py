# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:04:17 2020

@author: Administrator
"""

import re
myfile=open('sharp.txt',encoding='utf-8')
txt=myfile.read()
print('修改前内容：')
print(txt,'\n')
n=txt.count('#')
def find(str,n):
    out=str
    if(re.search('#',str)):
        rs=re.search('#.*(\n|.)',str).group()
        out=str.replace(rs,'')
    if(n!=0):
        return find(out,n-1)
    return out
txt=find(txt,n)
print('修改后内容：')
print(txt)