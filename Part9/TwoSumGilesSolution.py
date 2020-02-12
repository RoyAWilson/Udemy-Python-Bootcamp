# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:32:00 2020

@author: Roy
"""


def two_sum(nums, target):
    d =  {}
    
    for i in range(len(nums)):
        if target - nums[i] in d:
            print(d)
            return [d[target-nums[i]],i]
        
        d[nums[i]] = i
        
    return -1

L = [8, 6, 11, 3]
print(two_sum(L, 9))