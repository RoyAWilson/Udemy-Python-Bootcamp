# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:11:36 2019

@author: Roy
"""

## get 2 integers input and swap them in variables

integer_1 = (input('Please enter an integer: > '))
integer_2 = (input('Please enter a second integer: > '))

if integer_1.isdigit() and integer_2.isdigit():
    integer_1 = int(integer_1)
    integer_2 = int(integer_2)
    
    # swapper_1 = integer_1
    # swapper_2 = integer_2
    
    # integer_1 = swapper_2
    # integer_2 = swapper_1
    
    ## Giles' way was better:
    
    integer_1, integer_2 = integer_2, integer_1
    print(integer_1, integer_2)
else:
    print('One or more of your values were out of range.')
    