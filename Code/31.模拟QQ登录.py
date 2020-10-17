# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:15:14 2020

@author: Oliver
"""
from 布局测试 import test
from tkinter import Frame,StringVar,Label,Entry,Button,E,END,Tk
from tkinter.messagebox import showinfo,showwarning
root=Tk()
fup=Frame()
fup.pack()
username=StringVar()
password=StringVar()
label1=Label(fup,text='QQ账号:',width=8,anchor=E)
label1.grid(row=1,column=1)
entry1=Entry(fup,textvariable=username,width=20)
entry1.grid(row=1,column=2)

label2=Label(fup,text='密码:',width=8,anchor=E)
label2.grid(row=2,column=1)
entry2=Entry(fup,show='*',textvariable=password,width=20)
entry2.grid(row=2,column=2)

def reset():
    entry1.delete(0,END)
    password.set('')
def done():
    if(username.get()=='123456' and password.get()=='ABCD'):
        showinfo('成功',"登录成功")
        root.destroy()
        test()
    else:
        showwarning('失败',"登录失败")
    
fdown=Frame()
fdown.pack()
bt1=Button(fdown,text='重置',command=reset)
bt1.grid(row=1,column=1)
bt2=Button(fdown,text='确定',command=done)
bt2.grid(row=1,column=2)
label3=Label()
label3.pack()
root.mainloop()