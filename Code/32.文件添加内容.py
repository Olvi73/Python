# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:49:57 2020

@author: Oliver
"""

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

global file

def bt1click():
    global file
    file = askopenfile()
    if file:
        filestr = file.read()
        file.close()
        text1.delete('1.0', END)
        text1.insert('1.0', filestr)
        text1.focus()


def bt2click():
    global file
    data = text1.get('1.0', END)
    open(file.name, 'w+').write(data)
    showinfo('', '保存文件成功')


frame1 = Frame()
frame1.pack()
bt1 = Button(frame1, text='打开文件', command=bt1click)
bt2 = Button(frame1, text='保存文件', command=bt2click)
bt1.grid(row=0, column=0)
bt2.grid(row=0, column=1)
sc = Scrollbar()
sc.pack(side=RIGHT, fill=Y)
text1 = Text(yscrollcommand=sc.set)
text1.pack(expand=YES, fill=BOTH)
sc.config(command=text1.yview)
mainloop()
