# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:44:51 2019

@author: Roy
"""


addition = input('Please add a capital city to append to file :>')
while addition ==  '':
    addition = input('Please add a capital city to append to file :>')
f = open('capital.txt', 'a')
f.write(' ' + addition)
f.close()
f = open('capital.txt','r')
print(f.read())
f.close()