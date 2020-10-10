# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:44:29 2020

@author: Administrator
"""

class vector3:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return str((self.x,self.y,self.z))
    def __add__(self,v):    #加法
        s_x=self.x+v.x
        s_y=self.y+v.y
        s_z=self.z+v.z
        return vector3(s_x,s_y,s_z)
    def __sub__(self,v):    #减法
        s_x=self.x-v.x
        s_y=self.y-v.y
        s_z=self.z-v.z
        return vector3(s_x,s_y,s_z)
    def __mul__(self,num):  #乘法
        s_x=self.x*num
        s_y=self.y*num
        s_z=self.z*num
        return vector3(s_x,s_y,s_z)
    def __truediv__(self,num):    #地板除 __floordiv__  除法__truediv__
        s_x=self.x/num
        s_y=self.y/num
        s_z=self.z/num
        return vector3(s_x,s_y,s_z)

x1,y1,z1=map(int,input("请输入向量a:").split(" "))
x2,y2,z2=map(int,input("请输入向量b:").split(" "))
v1=vector3(x1,y1,z1)
v2=vector3(x2,y2,z2)
print("调用向量加法(a+b)：",v1+v2)
print("调用向量减法(a-b)：",v1-v2)

print("调用向量与标量除法(a/2)：",v1/2)
print("调用向量与标量乘法(b*3)：",v2*3)