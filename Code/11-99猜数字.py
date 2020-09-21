# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:56:08 2020

@author: Oliver
"""

print("请在11-99中猜一个数字，将它的十位与个位相加，然后用这个数减去相加之和，例如数字34，34-(3+4)=27，结果就是27")
x=list(range(1,82))
y=x[17:82:9]

while (1):
    var=input("结果为奇数还是偶数(奇数/偶数):")
    if var!='奇数' and var!='偶数':
        print("输入错误，请重新输入!")
    else:
        break;
if var=='奇数':
    first=y[1::2]
elif var =='偶数':
    first=y[::2]

while (1):
    var=input("结果是否大于50(是/否)：")
    if var!='是' and var!='否':
        print("输入错误，请重新输入!")
    else:
        break;
if var=='是':
    second=first[-2:]
elif var=='否':
    second=first[0:2]
check='是'
for answer in second:
    if check=='否':
        print("刚才是骗你的，其实你猜的数字是：",answer)
    else :
        print("你猜的数字是：",answer)
    check=input("是否正确：")
    if check=='是':
        print("世界上有很多不可思议的事情，其中之一就是我猜对了！")
        break;
    elif check=='否':
        continue;


