# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:43:18 2019

@author: Roy
"""


import random
import matplotlib

data = {}

letters = ['A', 'B', 'C', 'D' ,'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
           ,'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(letters)):
    data[letters[i]] = random.randint(1, 500)
print(data)
x, y = zip(*data.items())
#matplotlib.pyplot.barh(x, y)
matplotlib.pyplot.bar(x, y)
