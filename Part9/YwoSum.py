# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 20:01:20 2020

@author: Roy
"""

L = [2, 5, 3, 7, 4]
val_ret = []
val1 = 0
val2 = 0
match = False

for number in range(0,len(L)-1):
    if L[number] + L[number+1] == 10:
        val_ret.append(L[number])
        val_ret.append(L[number+1])
        match = True
        print(val_ret)
if match == False:
    print(-1)
    
        
        
#print(len(L))

# for nums in range(0, len(L)):
#     val1 = L[nums]
#     for numbers in range(1, len(L)-1):
#         #print(L[numbers])
#         val2 = L[numbers+1]
#         if numbers == len(L):
#             print(-1)
#         elif val1 + val2 == 10:
#              val_ret.append(val1)
#              val_ret.append(val2)
#              print(val_ret) 

          