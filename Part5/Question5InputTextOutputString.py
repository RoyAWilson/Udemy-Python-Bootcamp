# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:57:42 2019

@author: Roy
"""

## Input string of number between 1 and five and output text.  Force input to lower


my_text = input('Enter a number between 1 and 5 as text >>> ')
my_text = my_text.lower()

if my_text == 'one':
    print(1)
elif my_text == 'two':
    print(2)
elif my_text == 'three':
    print(3)
elif my_text == 'four':
    print(4)
elif my_text == 'five':
    print(5)
else:
    print('Out of range.')