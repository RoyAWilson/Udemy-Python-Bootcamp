# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:05:41 2019

@author: Roy
"""
d1 = {}
companies = ['Python DS', 'Pysoft', 'Pythazon', 'Pybook']
keys = ['Open', 'Close', 'Low', 'High']
data = [[12.87, 13.33, 11.42, 13.10], [23.54, 25.76, 21.87, 22.33], [98.99, 102, 97.21, 100.063], [203.63, 207.54, 202.43, 205.24]]
for i in range(len(keys)):
    d1[companies[i]] = dict(zip(keys, data[i]))
print(d1)
