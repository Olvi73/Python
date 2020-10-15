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
        if(re.search('#(.*)\n',str)):
            rs0=re.search('#(.*)\n',str).span()[0]
            rs1=re.search('#(.*)\n',str).span()[1]
            temp=str[rs0:rs1]
            out=str.replace(temp,'')
        else:
            rs=re.search('\n#',str).span()[0]
            out=str[:rs]
    if(n!=0):
        return find(out,n-1)
    return out
txt=find(txt,n)
print('修改后内容：')
print(txt)