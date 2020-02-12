# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:56:29 2019

@author: Roy
"""
## To write to a new or existing file:

# f = open('Kippling.txt', 'w')
# print(type(f))

# f.write('If you can keep your head while all about are losing theirs and blaming it on you,\n')

# f.write('If you can trust yourself when all men doubt you,\n But make allowances for their doubting too;\n')

# f.write('If you can wait and not be tired by waiting,\n Or being lied about don\'t deal in lies,\n')

# f.write('Or being hated, don\'t give way to hating,\nAnd yet don\'t look too good or talk too wise\n')

# f.close()

## To Open an existing file to read:

# f = open('Kipling.txt','r')
# print(type(f))
# print(f.read())
# f.close()

## Using the readline() method

# f = open('Kipling.txt','r')
# print(f.readline())
# f.close()

## The readlines() method

# f = open('Kipling.txt','r')
# print(f.readlines())
# f.close()

## Using readlines to add values to an iterable variable:

# f = open('Kipling.txt','r')

# print(type(f))

# content = f.readlines()
# f.close()

## Appending content to a file

# f = open('Kippling.txt','a')
# f.write('If you can dream, and not make dreams your master;\nIf you can think and not make thoughts your aim;\n')
# f.close()
# print()
# f = open('Kippling.txt','r')
# print(f.read())
# f.close()

## Printing out contents with a with statement NB one does not have to close the open file as done automatically with this statement
## end = '' as print automatically adds a line feed per line of text and we have line break characters in the file.

with open('Kippling.txt','r') as f:
    for line in f.readlines():
        print(line, end = '')
        