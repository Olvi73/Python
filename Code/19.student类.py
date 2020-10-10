# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class student:
    def Input(self,c1,c2):
        self.c1=c1
        self.c2=c2
    def Show(self):
        Sums=self.c1+self.c2
        Avgs=(self.c1+self.c2)/2
        print("总分：",Sums,"  平均分：",Avgs)
        
x=student()
c1=int(input("请输入第一门成绩："))
c2=int(input("请输入第二门成绩："))
x.Input(c1,c2)
x.Show()