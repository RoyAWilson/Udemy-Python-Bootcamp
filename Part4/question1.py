# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:31:06 2019

@author: Roy
"""

## Write program to get user to input the radius of a circle and work out the area - Area = pi r ^2

radius = float(input('Please enter the radius of the circe\n >>> '))
pi = 3.14159
area = pi * radius ** 2
print('The area of a circle with radius ', radius, ' is ', area)
print(f'the area of your circle with radius {radius} is {area}')