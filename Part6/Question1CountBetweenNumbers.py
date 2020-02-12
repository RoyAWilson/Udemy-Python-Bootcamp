# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:13:57 2019

@author: Roy
"""

# ## to count between 2 numbers in the range 1 to 1oo
# lower_limit = 0
# higher_limit = 101

# while lower_limit <= 0 or higher_limit >100:
#     print('Please enter 2 numbers in the range 1 to 100 inclusive:')
#     lower_limit = int(input('Please enter lower number:> '))
#     higher_limit = int(input('Please enter upper limit:> '))

# # print(lower_limit)
# # counter = 1
# # for i in range(lower_limit,higher_limit,1):
    
# #     print(lower_limit + counter)
# #     counter += 1


# ## And using while loop

# print(lower_limit, end = ' ')
# while lower_limit < higher_limit:
#     print(lower_limit + 1, end = ' ')
#     lower_limit = lower_limit + 1

    
## Giles' solution:

# lower_limit = int(input('Please enter an number between 1  and 100:> '))
# higher_limit = int(input('Please enter an number between 1  and 100:> '))
# while lower_limit < 0 or lower_limit > 100 or higher_limit < 0 or higher_limit > 100 or lower_limit == higher_limit:
#     print('Numbers must be different values between 1 and 100, try again')
#     lower_limit = int(input('Please enter an number between 1  and 100:> '))
#     higher_limit = int(input('Please enter an number between 1  and 100:> '))
# if lower_limit < higher_limit:
#     for i in range(lower_limit, higher_limit+1):
#         print(i, end=' ')
# else:
#     for i in range(higher_limit, lower_limit+1):
#         print(i, end = ' ')
        
# And checking for numeric input:

lower_limit = input('Please enter an number between 1  and 100:> ')
higher_limit = input('Please enter an number between 1  and 100:> ')
while not lower_limit.isdigit() or not higher_limit.isdigit():
    print('Your entry is invalid, please enter only digits!')
    lower_limit = input('Please enter an number between 1  and 100:> ')
    higher_limit = input('Please enter an number between 1  and 100:> ')

higher_limit = int(higher_limit)
lower_limit = int(lower_limit)
    
while lower_limit < 0 or lower_limit > 100 or higher_limit < 0 or higher_limit > 100 or lower_limit == higher_limit:
    print('Numbers must be different values between 1 and 100, try again')
    lower_limit = int(input('Please enter an number between 1  and 100:> '))
    higher_limit = int(input('Please enter an number between 1  and 100:> '))
if lower_limit < higher_limit:
    for i in range(lower_limit, higher_limit+1):
        print(i, end=' ')
else:
    for i in range(higher_limit, lower_limit+1):
        print(i, end = ' ')    