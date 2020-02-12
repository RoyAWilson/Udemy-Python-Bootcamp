# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:56:33 2019

@author: Roy
"""

## Get 2 integers input and output product if both >15, sum if one >15 or 0 if neither > 15

print('Enter 2 integers between 1 and 20:\n')
number_1 = input('Enter the first number: >> ')
number_2 = input('Enter second number: >> ')

if number_1.isdigit() and number_2.isdigit():
    number_1 = int(number_1)
    number_2 = int(number_2)
    if number_1 > 15 and number_2 > 15:
        print('The product of your numbers is', number_1 * number_2)
    elif number_1 + number_2 >= 16:
        print('the sum of your numbers is', number_1 + number_2)
    elif number_1 < 15 and number_2 < 15:
        print(0)
else:
    print('I asked for 2 integers!')