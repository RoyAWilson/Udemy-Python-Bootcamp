# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 20:34:07 2019

@author: Roy
"""


# my_list = [[1, 2, 3],[4, 5, 6],[7, 8,9]]

#countries = {'France':{'capital':'Paris','laguage':'French'}, 'Spain':{'capital':'Madrid','language':'Spanish'}, 'United Kingdom':{'capital':'London','language':'English'}','India':{'capital':'New Dehli','language':'many'},'United States':{'capital':'Washington DC','language':'American English'},'Italy':{'capital':'Rome','language':'Italian'},'Denmark':{'capital':'Copenhagen','language':'Danish'},'Germany':{'capital':'Berlin','language':'German'},'Greece':{'capital':'Athens','language':'Greek'},'Bulgaria':'capital':'Sofia','language':'Bulgarian'},'Ireland':{'capital':'Dublin','language':'Celtic'},'Mexico':{'capital':'Mexico City','language':'Portugese'}}
countries = {'France':{'Capital':'Paris','Language':'French'},'Spain':{'Capital':'Madrid','Language':'Spanish'},
            'United Kingdom':{'Capital':'London','Language':'English'},
            'United States':{'Capital':'Washington DC','Language':'English'},
            'Italy':{'Capital':'Rome','Language':'Italian'}
            }

for key, value in countries.items():
    print(key, value)

for key, value in countries.items():
    print(f'{value["Capital"]} is the capital of {key}.  They speak {value["Language"]}')
    