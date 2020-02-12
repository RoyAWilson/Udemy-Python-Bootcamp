# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:24:47 2019

@author: Roy
"""

## find all odd numbers between 1 and 100 and add to list odd and all evens to list even

even = []
odd = []

for i in range(1,100):
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)
print(f'The odd numbers are: {odd}\n The even numbers are {even}')

## could also "if not i % 2: - would be same