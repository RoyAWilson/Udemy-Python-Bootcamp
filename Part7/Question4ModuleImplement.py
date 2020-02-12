# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:54:41 2019

@author: Roy
"""

import imghdr
import turtle
import random


imgtyp = imghdr.what('JPSean.jpeg')
print(imgtyp)
turtle.color('red', 'yellow')
for i in range(1, 5 ):
    for turns in range(1,24):
        turtle.forward(25)
        turtle.right(15)
        turtle.forward(25)
        turtle.back(25)
        
print('done')