# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:33:25 2019

@author: Roy
"""

## swap name order christian name surname to surname christian name:

c_name = input('Please enter your christian name: > ')
s_name = input('Please enter your surname: > ')

c_name, s_name = s_name + ',', c_name

print(c_name, s_name)
