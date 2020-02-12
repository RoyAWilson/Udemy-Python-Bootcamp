# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:41:27 2020

@author: Roy
"""


# write a class to take the radius of a circle and calculate the area

class AreaCircle(object):
    '''
    pi: Constant value 3.14159
    radius: User input radius of circle
    area: Calculated pi r squared
    '''
    
    def __init__(self, pi=3.14159, radius=0.0):
        self.pi = pi
        self.radius = radius
        
    def area(self):
        self.radius = float(input('Please give the radius of the circle > '))
        area = self.pi * (self.radius ** 2)
        print(f'The area of circle radius {self.radius} is {area}')
        