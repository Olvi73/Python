# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:49:18 2020

@author: Administrator
"""

class Bank:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def Deposit(self,money):
        self.money+=money
    def Withdraw(self,money):
        self.money-=money

name=input("请输入用户名：")
money=float(input("请输入余额："))
user=Bank(name,money)
while True:
    print("当前用户名：%s   当前余额：%d元"%(user.name,user.money))
    print("1、存钱  2、取钱  3、退出")
    option=float(input(""))
    if option==1:
        m=float(input("请输入存入钱数："))
        user.Deposit(m)
        continue
    elif option==2:
        m=float(input("请输入取出钱数："))
        user.Withdraw(m)
        continue
    elif option==3:
        print("感谢使用！")
        break
    else:
        print("输入错误!")
        continue