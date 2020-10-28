# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
x=random.randint(0,100)
print("成绩为：",x)
if x>=90:
    print("A")
elif x<90 and x>=80:
    print("B")
elif x<80 and x>=70:
    print("C")
elif x<70 and x>=60:
    print("D")
elif x<60:
    print("E")