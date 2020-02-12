# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:34:24 2019

@author: Roy
"""


## Create a dictionary with four suits of cards

deck = {}
suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
faces = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King' ]

for i in suits:
      deck[i] = faces
print(deck)

