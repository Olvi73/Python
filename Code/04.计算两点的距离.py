# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:15:59 2020

@author: Oliver
"""

'''
输入平面坐标系两点的坐标，计算显示两点间的距离。
计算坐标两点间的距离公式为：s=√((x_b-x_a )^2+(y_b-y_a )^2 )
'''

import math
temp=input("请输入a的坐标:")
a=[int(n) for n in temp.split(',')]
temp=input("请输入b的坐标:")
b=[int(n) for n in temp.split(',')]
rs=math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
print('a与b的距离为:%.2f' %rs)
