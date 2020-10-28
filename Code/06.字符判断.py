# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:54:17 2020

@author: Administrator
"""

var=input("请输入一个字符：")
if var.isupper()==True:
    print("输入的字符是大写字母")
elif var.islower()==True:
    print("输入的字符是小写字母")
elif var.isdecimal()==True:
    print("输入的字符是数字")
else:
    print("输入的字符是其他字符")