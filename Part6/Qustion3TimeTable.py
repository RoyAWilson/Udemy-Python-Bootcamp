# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:12:03 2019

@author: Roy
"""

## Display a multiplication table for an input number
num_1 = input('Please enter a number :> ')
while not num_1.isdigit():
    print('I can only accept numeric values, try again')
    num_1 = input('Please Enter a number:> ')
num_1 = int(num_1)
iterate = 13
for i in range(1, iterate):
    print(f'{i} x {num_1} = {num_1 * i} ', end = ' ')
    