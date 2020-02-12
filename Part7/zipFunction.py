# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 19:23:07 2019

@author: Roy
"""


# my_list1 = [1,2,3,4]
# my_list2 = ['a', 'b', 'c', 'd']
# joined = list(zip(my_list1, my_list2))
# print(f'The result of zip is: {joined} of type {type(joined)}')

# i, j = zip(*joined)

# print(i, j)

capitals = {'France':'Paris', 'Spain':'Madrid', 'United Kingdom':'London','India':'New Dehli','United States':'Washington DC','Italy':'Rome','Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens','Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'}

print(capitals.items())

x, y = zip(*capitals.items())
