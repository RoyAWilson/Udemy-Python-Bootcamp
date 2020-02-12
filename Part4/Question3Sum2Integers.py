# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:00:59 2019

@author: Roy
"""

## to sum 2 integers input by the user

value1 = int(input('Please input first number to sum >>> '))
value2 = int(input('Please input the second number to sum >>> '))
aggregate = value1 + value2
print('The sum of ', value1, ' and ', value2, ' is: ', aggregate)

## or the following also works

print('The sum of ' + str(value1) + ' and ' + str(value2) + ' is ' + str(value1 + value2))
## str() forces the value in the int valueX into a string type so it can be concatted to the printed string
