# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:11:03 2019

@author: Roy
"""


capitals = {'France':'Paris', 'Spain':'Madrid', 'United Kingdom':'London','India':'New Dehli','United States':'Washington DC','Italy':'Rome','Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens','Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'}

# question = input('Please enter a country to find the capital:>')

# if not question in capitals:
#     print('Sorry, that country is not in my list.')
# else:
#      print(f'The capital of {question} is: {capitals[question]}')


question = input('Please enter a country to find the capital :> ')
while not question in capitals:
    print('Sorry, I do not have that country in my list')
    question = input('Please enter a country to find the capital :> ')
print(f'The capital of {question} is: {capitals[question]}')
