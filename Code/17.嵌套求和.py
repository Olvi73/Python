# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:07:45 2020

@author: Administrator
"""

var=input("输入列表的值：")

#ls=['1','3','2','12','14','52']
ls=[int(n) for n in var.split(" ")]
def sumlist(ls,s):
    if(len(ls)==0):
        print("循环结束")
        return s
    else:
        s+=int(ls[0])
        ls.pop(0)
        print("循环还剩下%d次"%(len(ls)))
        return sumlist(ls,s)
print(sumlist(ls,0))