# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:54:19 2020

@author: Oliver
"""

import wordcloud,cv2
text='Is it just  me or  this  world  is getting crazy out  there? ​​​​Your hair is winter fire, January embers. My heart burns there, too. Why think separately of this life and the next when one is born from the last.'
img=cv2.imread('Cloud.jpg')
cloud=wordcloud.WordCloud(mask=img,background_color="white",width=1000,height=1000,font_path="C:\\Users\\Oliver\\AppData\\Local\\Microsoft\\Windows\\Fonts\\ProductSans-Regular.otf").generate(text)
cloud.to_file('English_clo ud.jpg')


#font Roboto-Regular.ttf  OCRAEXT.TTF  RegencyRegular.ttf
#C:\Users\Oliver\AppData\Local\Microsoft\Windows\Fonts