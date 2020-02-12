# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:06:39 2019

@author: Roy
"""

## Convert inches to cm

inches = float(input('Please input measurement in Inches\n >'))
convert = 2.54
cms = inches * convert
print(f'{inches} inches is equal to {cms} centimetres')