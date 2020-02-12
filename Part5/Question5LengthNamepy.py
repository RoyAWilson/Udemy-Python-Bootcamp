# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:43:59 2019

@author: Roy
"""

name = input('Please enter your name: >>> ')
# if name.istext():
if name.isdigit():
    print('You entered a number!')
else:
    letters = len(name)
    if letters >= 5:
        print(f'Your name, {name} is {letters} letters long')
    else:
        print('Your name is a secret')
