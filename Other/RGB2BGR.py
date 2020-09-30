# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:50:35 2020

@author: Oliver
"""

from PIL import Image
im = Image.open("1.jpg")
r,g,b,= im.split()
rgb_image = Image.merge('RGB',(b,g,r))
rgb_image.show()