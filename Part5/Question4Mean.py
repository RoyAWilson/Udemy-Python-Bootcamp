# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:40:13 2019

@author: Roy
"""

## Input range of numbers and calculate the mean print to screen

numbers = []
user_input  = input('Please input a number. Exit to finish :> ')
while user_input.lower() != 'exit':
    while not user_input.isdigit():
        print('Enter only numbers or Exit, please')
        user_input = input('Please enter a number, exit to finish :> ')
    numbers.append(int(user_input))
    user_input = input('Next number of exit to finish :> ')
    total = 0
for number in numbers:
    total += number
if len(numbers) < 1:
    print('Goodbye!') ## Added this as typing exit before entering numbers caused crash.
else:
    print(f'The mean is {total/len(numbers)}')
    print(sum(numbers)/len(numbers))

# user_input = input('Please enter a number type exit to stop:> ')
# numbers = []
# while user_input.lower() != 'exit':
#     while not user_input.isdigit():
#         print('That is not a number! Numbers only please:> ')
#         user_input = input('Try again:> ')
#     numbers.append(int(user_input))
#     user_input = input('Please enter next number:> ')
# total = 0
# for number in numbers:
#     total += number

# print(f'Mean is {total/len(numbers)}')    
# print(sum(numbers)/len(numbers))