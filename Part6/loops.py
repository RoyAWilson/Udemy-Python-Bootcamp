# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:38:00 2019

@author: Roy
"""

# Loops

# For loops


# for i in range(10):
#     print(i)

#print()

# for i in range(10):
#     print(i,end=' ')
    

# for i in range(1, 10):
#     print(i, end=' ')

#for i in range(1, 11):
    #print(i, end=' ')

# help(range)

# for i in range(0,101,4):
#     print(i, end = ' ')
    
# for i in range(100,0,-1):
#     print(i, end = ' ')

# word = 'python'
# # for i in word:

# #     print(i)
# for char in  word:
#     print(char)



# A little more on Variables and Introducing Lists:

# x = 5
# x
# x = x + 1

# print(f'x = {x}')

# x += 1

# print(f'x = {x}')

# y = x

# print(f'y = {y}')

# x += 1

# print(f'x = {x}')

# print(f'y = {y}')


## Lists

data = [53, 76, 25, 98, 56, 42, 69, 81]

# data_1 = []

# for num in data:
#     print(num, end=' ')


# total = 0
# for num in data:
#     total = total + num
# print(f'sum of \'data\' is {total}')

# total_2 = sum(data)
# print(f'total_2 = {total_2}')

## Find max value

# find_max = 0
# for num in data:
#     if num > find_max:
#         find_max = num
# print(f'Max value is {find_max}')

## Find max using built in function:

# print(f'Max value using Python Function \'max\' {max(data)}')

# my_list = [1, 11, 21, 31, 41, 51]
# for i in range(6):
#     print(my_list[i])

# for i in range(5):
#     print(my_list[i])
#     print(my_list[i+1])

## Bubble sort
# data_copy = data[:]
# for i in range(len(data_copy)):
#     for j in range(0,len(data_copy)-i-1):
#         if data_copy[j] > data_copy[j+1]:
#             data_copy[j],data_copy[j+1] = data_copy[j+1],data_copy[j]
# print(data_copy)

# print(f'Data sortd by python function \'sorted\' {sorted(data)}')


# my_list = [34, 76, 58]

# my_list.append(100)

# my_list.remove(34)

# my_list.reverse()

# my_list.extend([67, 68, 69])

# print(my_list.index(67))

# n = 10

# while n > 0:
#     print(n)
#     n = n-1

# user_input = int(input('Please enter ages of class member. Type -1 to end:>'))
# ages = []
# while user_input > 0:
#     ages.append(user_input)
#     user_input = int(input('The next age:>'))
# print('The ages are',ages)  

# count = 0
# class_names = []
# name = input('Please enter name (type n to end) :>')  
# while name != 'n':
#     count += 1
#     class_names.append(name)
#     print(f'{name} has  been added.')
#     name = input('Next name? > ')
# print(f'There are {count} people in the class, they are {class_names}')


## Fizzbuzz using modulus

n = 100

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'Fizzbuzz!!!!')
    elif i % 5 == 0:
        print(i, 'Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
