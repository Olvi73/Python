# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

myfile=open('py.txt',encoding='utf-8')
x=myfile.read()
print('输出原文件内容:')
print(x,'\n')
StrFile=[str(s) for s in x]
for i in range(len(StrFile)):
    if(StrFile[i].isalpha()):
        if(StrFile[i].islower()):
            StrFile[i]=StrFile[i].upper()
        else:
            StrFile[i]=StrFile[i].lower()
    else:
        continue
print("输出文件内容:")
print(''.join(StrFile),'\n')