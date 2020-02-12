# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:41:04 2019

@author: Roy
"""

## To get integer input between 1 and 5 and output as a string

my_number = int(input('Enter a number between 1 and 5 >>> '))
if my_number <1 or my_number >5:
    print(f'{my_number} MUST be between 1 and 5 and an integer')
elif my_number == 1:
        print('One')
elif my_number == 2:
    print('Two')
elif my_number == 3:
    print('Three')
elif my_number == 4:
    print('Four')
elif my_number == 5:
    print('Five')