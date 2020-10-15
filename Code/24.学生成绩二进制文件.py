# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:08:02 2020

@author: Oliver
"""
import pickle
dict={'name':('john','bob','jack'),'score':('80','90','65')}
file=open('data.dat','wb')
pickle.dump(dict,file)
file.close()
f=open('data.dat','rb')
dic=pickle.load(f)
for n in range(3):
    print(dic['name'][n],end='  ')
    print(dic['score'][n])