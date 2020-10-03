# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:26:34 2020

@author: Administrator
"""

     
n=int(input("输入杨辉三角的层数："))
list=[]
def tri(layer):
    l=[]
    count=layer
    for c in range(layer):
        row=[1]
        l.append(row)
        for n in range(count):
            if(layer<=5):
                print(" ",end="")
            else:
                print("  ",end="")
        if c==0:
            for num in row:
                if(layer<=5):
                    print(" %d"%num,end="")
                else:
                    print("  %d"%num,end="")
                print()
            continue
        for m in range(1,c):
            row.append(l[c-1][m-1]+l[c-1][m])
        row.append(1)
        for num in row:
            if(layer<=5):
                print(num,end="  ")
            else:
                if(10<=num<100):
                    print(num,end="  ")
                elif(num>=100):
                    print(num,end=" ")
                else:
                    print(num,end="   ")
        print()
        count-=1
    
tri(n)