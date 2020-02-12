# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:07:32 2019

@author: Roy
"""

## Draw an F with asterisks

print('*****\n*\n*****\n*\n*\n*')

five = '*****'
one = '*'

print(f'{five}\n{one}\n{five}\n{one}\n{one}\n{one}')

## Giles' solution

# star = '*'

# for i in range(1,7):
#     for j in range(1,6):
#         if i == 1 and j < 6:
#             print(star, end = '')
#         elif i == 2 and j == 1:
#             print()
#             print(star)
#         elif i == 3 and j < 5:
#             print(star, end = '')
#         elif i == 4 and j == 1:
#             print()
#             print(star)
#         elif i == 5 and j == 1:
#             print(star)
#         elif i == 6 and j == 1:
#             print(star)