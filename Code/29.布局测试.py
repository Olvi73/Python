# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:01:14 2020

@author: Oliver
"""

from tkinter import Tk,Label

def test():
    root=Tk()
    root.title("测试布局")
    root.geometry("280x80")
    
    label1=Label(text='标签一')
    label2=Label(text='标签二')
    label3=Label(text='标签三')
    
    label1.grid(row=0,column=3)
    label2.grid(row=1,column=1)
    label3.grid(row=2,column=2)
    # label1.pack()
    # label2.pack()
    # label3.pack()
    # label1.place(x=0,y=20)
    # label2.place(x=30,y=50)
    # label3.place(x=100,y=0)
    root.mainloop()
test()