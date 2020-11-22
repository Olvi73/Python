# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 08:56:44 2020

@author: Oliver
"""

n=int(input(""))
score=input("")
score=[int (n) for n in score.split(" ")]
sumScore=0
count=0
temp=0
maxs=0
mins=101
for i in score:
    sumScore+=i
    count+=1
    if i>maxs:
        maxs=i
    if i<mins:
        mins=i
    if count>=3:
        temp=sumScore
        temp=temp-maxs-mins
        print ("%.2f"%(temp/(count-2)))