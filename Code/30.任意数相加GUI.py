# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:39:23 2020

@author: Administrator
"""

from tkinter import Tk,StringVar,Label,Entry,Button

root=Tk()
root.title("任意数相加")
root.geometry("500x80")
def plus():
    sum=float(numA.get())+float(numB.get())
    print('%s+%s=%.2f'%(numA.get(),numB.get(),sum))
    ans.set(sum)


numA=StringVar()
numB=StringVar()
ans=StringVar()

label1=Label(text='+')
label2=Label(text='=')
entry1=Entry(root,textvariable=numA,width=10)

entry2=Entry(root,textvariable=numB,width=10)

entry3=Entry(root,textvariable=ans,width=10)
bt1=Button(root,text='相加',command=plus,width=10)


entry1.place(x=50,y=0)
label1.place(x=150,y=0)
entry2.place(x=200,y=0)
label2.place(x=300,y=0)
entry3.place(x=350,y=0)
bt1.place(x=200,y=40)
root.mainloop()
    
    