# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:27:12 2019

@author: Roy
"""

## Produce times tables 1 - 12 no user input:

iterate = 12
num_1 = 2
for i in range(1, iterate):
    for i_2 in range(1,13):
        print(f'{i_2} x {num_1} = {num_1 * i_2} ', end = ' ')
    num_1 = num_1 + 1
    
    