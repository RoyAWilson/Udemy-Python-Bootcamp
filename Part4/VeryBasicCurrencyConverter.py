# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:57:43 2019

@author: Roy
"""

## conslidate learning with own example. Simple currency converter

currency_1 = float(input('Please input amount of to convert\t >>>'))
conversion_rate = float(input('Please input the conversion factor\t >>>'))
currency_2 = currency_1*conversion_rate
print(f'At conversion rate {conversion_rate} your {currency_1} will be worth {currency_2}')
