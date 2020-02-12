# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 21:16:21 2019

@author: Roy
"""

## write code to pring the factorial of 15

# fac = 15
# ans = 1

# for i in range(1,fac+1):
#     ans = ans * i

# print(f'The factorial of {fac} is {ans}')

## supplimentary do above with user input:

ans =1
fac = input('Enter a number to find the factorial:> ')
while not fac.isdigit():
    print('Enter a positive value, no text please')
    fac = input('Enter a number to find the factorial :> ')
fac = int(fac)
if fac < 1:
    fac = input('You must enter a digit greater than 0 please :>')
else:
    fac = int(fac)
    for i in range(1,fac+1):
        ans = ans * i
print(f'The factorial of {fac} is {ans}')