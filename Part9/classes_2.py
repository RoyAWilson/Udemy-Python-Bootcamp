# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:51:29 2020

@author: Roy
"""


class Patient(object):
    ''' 
    Medical Centre Patient 
    Attributes
    -----------
    name: Patient name
    age: Patient age
    conditions: Existing medical conditions
    '''

# Class variable
    
    status = 'patient'
    
    # Constructor for class patient with instance variables name and age
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []
        
        #Methods
        
    def get_details(self):
        print(f'Patient record: {self.name}, {self.age} years. Current information: {self.conditions}')
    def add_info(self, information):
        self.conditions.append(information)
        
#steve = Patient('Steven Hughes', 48)
#abigail = Patient('Abigail Sandwick', 32)

## INHERITANCE
        
class Infant(Patient):
    
    ''' Patient under 2 years of age '''
    
    def __init__(self, name, age):
        self.vaccinations = []
        super().__init__(name, age)
        
    def add_vac(self, vaccine):
        self.vaccinations.append(vaccine)
        
    def get_details(self):
        print(f'Patient record: {self.name}, {self.age} years'
              f'Patient has had {self.vaccinations} vaccines.'
              f'Current Information: {self.conditions}'
              f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')
        print(self.status)
archie = Infant('Archie Fittleworth', 0)
archie.add_vac('MMR')