# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:50:16 2019

@author: Roy
"""

## Convert entered deg f to deg c

farenheit = float(input('How many degrees farenheit?\n\t >>>'))
centigrade = (farenheit - 32) * 5/9
print(farenheit, 'degrees farenheit =', centigrade, ' degrees centigrade')
