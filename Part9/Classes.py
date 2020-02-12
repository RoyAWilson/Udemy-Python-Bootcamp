# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:39:03 2019

@author: Roy
"""


# x = 1

# y = [1, 2, 3]

# z = {'a' : 1}


class Patient(object):
    ''' Attributes
        ----------
        name - Patient name
        age -- Patient age
        conditions -- Existing conditions
        '''
        
    status = 'Patient'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []
    
    def get_details(self):
        print(f'Patient record {self.name}, {self.age} years\n'
              f'Current information: {self.conditions}')
        
    def add_info(self, information):
        self.conditions.append(information)

steve = Patient('Steven Hughes', 48)
abigail = Patient('Abigail Sandwick', 32)

##Create a class with inheritance from the patient class:

class Infant(Patient):
    ''' Patient under 2 years of age '''
    def __init__(self, name, age):
        self.vaccinations = []
        super().__init__(name, age)
        
    def add_vac(self, vaccine):
        self.vaccinations.append(vaccine)
        
    def get_details(self):
        print(f'Patient record {self.name}, {self.age} years'\
              f'\n {self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')
archie = Infant('Archie Fittleworth', 0)
archie.add_vac('MMR')
