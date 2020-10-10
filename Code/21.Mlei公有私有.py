# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:18:45 2020

@author: Administrator
"""

class Mlei:
    name="Leya"
    sex="woman"
    __age=25
    __weight=50
    def GetInfo(self):
        return print("name:%s,sex:%s"%(self.name,self.sex))
    def __GetMoreInfo(self):
        return print("age:%s,weight:%s"%(self.__age,self.__weight))
c1=Mlei()
c2=Mlei()
print("访问公有类属性：",c1.name,c1.sex)
print("访问公有类方法：",end=' ')
c1.GetInfo()
c2.name='Maya'
