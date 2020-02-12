# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:21:19 2019

@author: Roy
"""


## Write code to populate a dictionary with the first 12 values in fibonacci sequence

n = 12
a = 0
b = 1
d = dict()
for i in range(1,n+1):
    d[i] = a
    a, b = b, a + b
print(d)
