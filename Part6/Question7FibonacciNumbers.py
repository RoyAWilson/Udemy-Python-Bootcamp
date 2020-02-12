# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:37:30 2019

@author: Roy
"""

## To Print the first 2 Fibonacci numbers starting at zero in a list

# counter = 0
# num_start = 0
# fib_sequence = []
# fib_sequence.append(num_start)
# num_start += 1
# fib_sequence.append(num_start)
# while counter < 18:
#     num_start = num_start + fib_sequence[-2]
#     fib_sequence.append(num_start)
#     counter += 1
# print(f'The first 20 numbers in the Fibonacci sequence are: {fib_sequence}')

##Giles' code slightly different than mine.

n = 20
a = 0
b = 1

fib_nums = []

for i in range(n):
    fib_nums.append(a)
    a,b = a+b, a
print(f'The first {n} fibonacci numbers are: {fib_nums}')

## Had to change his code slightly to get it to work - swapped orfer of a,b = from a, a + b