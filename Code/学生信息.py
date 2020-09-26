# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:45:59 2020

@author: Administrator
"""

stu={}
n=int(input("请输入学生人数:"))
for i in range(n):
    info=input("请输入学号和姓名并用空格隔开：")
    list=info.split(' ')
    id=list[0]
    name=list[1]
    stu[id]=name
order=sorted(stu.items(),key=lambda x:x[0],reverse=False)
opid=[x[0] for x in order] 
opname=[x[1] for x in order] 
for i in range(n):
    print("学号："+''.join(opid[i])+"   姓名："+''.join(opname[i]))

