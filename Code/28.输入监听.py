# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:56:24 2020

@author: Administrator
"""

from tkinter import Tk,Entry,Frame

def showmsg(event):
   if(event.num==1):
       print("按下鼠标左键")
   elif(event.num==2):
       print("按下鼠标中键")
   elif(event.num==3):
       print("按下鼠标右键")
def showkeymsg(event):
   print("你按下了：",event.keysym)
   
root=Tk()
root.title("鼠标键盘监听")
entry=Entry(root)
entry.bind("<Key>",showkeymsg)

frame=Frame(root,width=300,height=300)
frame.bind("<Button>",showmsg)
frame.pack()
entry.pack()

root.mainloop()

