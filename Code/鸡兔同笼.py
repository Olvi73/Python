# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:47:53 2020

@author: Oliver
"""
'''
编写程序，求解鸡兔同笼问题。一个笼子中有鸡X只，兔Y只，每只鸡有2只脚，
每只兔有4只脚。若鸡和兔的总头数为H，总脚数为F。
输入总头数和总脚数，输出笼中鸡和兔的数。
'''
head=int(input('请输入总头数：'))
foot=int(input('请输入总脚数：'))
y=(foot-(2*head))/2
x=(head-y)
print('鸡有：',int(x),'只',)
print('兔有：',int(y),'只')