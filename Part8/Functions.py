# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 18:04:49 2019

@author: Roy
"""


#print('Hello World!')

# def hello():
#     print('Hello, World!')
# hello()

# for i in range(5):
#     hello()

## Function with an argument

# def hi(name):
#     print(f'Hello, {name}!')
# hi('Roy')
# hi('Anthony')

## Function with argument and default value:

# def hi_2(name = 'Roy'):
#     print(f'Hello, {name}!')
# hi_2()


## Fibonacci sequence in function next lines reminder how to calculate the number

# n = 20
# a = 0
# b = 1

# for i in range(n):
#     a,b = b, a + b
# print(b)

## Fibonacci as a function

# def fib(n):
#     a = 0
#     b = 1

#     for i in range(n):
#         a,b = b, a + b
#     return a

# choose = int(input('Enter a number for the fibonacci set :> '))
# fib_num = fib(choose)
# print(fib_num)
# I changed this to allow user input

##Using above function in a loop to produce the fibonacci sequence for given number of numbers

# def fib(n):
#     '''Generates the nth fibonacci number'''
#     a = 0
#     b = 1

#     for i in range(n):
#         a,b = b, a + b
#     return a

# choose = int(input('Enter a number for the fibonacci set :> '))
# for i in range(choose):
    
#     fib_num = fib(choose)
#     print(fib(i))

## Calculate the mean:

# def calc_mean(first, *remainder):
#     ''' Calculates the mean of numbers'''
#     mean = (first + sum(remainder)) / (1 + len(remainder))
#     return mean
# print(calc_mean(23,41,56,76,45))


## Recursion

# def fib_2(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib_2(n-1) + fib_2(n-2)

# x = fib_2(20)
# print(x)

## More on functions

# def sum_and_mult(a,b):
#     total = a + b
#     product = a * b
#     return total, product
# func_call = sum_and_mult(1, 4)
# print(func_call)
# print(type(func_call))

# var_1, var_2 = sum_and_mult(6, 7)
# print(var_1, var_2)
# print(type(var_1), type(var_2))

# var_3, var_4 = 5, 6

# def add1(var_3, var_4):
#     var_3 = var_3 + 1
#     var_4= var_4 + 1
#     print(f'inside the function var_3 = {var_3} and var _4 = {var_4}')
#     return var_3, var_4
# add1(18, 19)
# print(f'The value outside the function var_3 {var_3} and var_4 {var_4} ')


# def lengthen_list(n, my_list = [1, 2, 3]):
#     my_list.append(n)
#     return my_list
# x = lengthen_list(4)
# x = lengthen_list(4)
# x = lengthen_list(4)

def lengthen_list_2(n, my_list = None):
    if my_list == None:
        my_list = [1, 2, 3]
        my_list.append(n)
        return my_list
    
y = lengthen_list_2(4)
y = lengthen_list_2(4)
y = lengthen_list_2(4)