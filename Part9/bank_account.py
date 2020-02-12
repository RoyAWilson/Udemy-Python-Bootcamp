# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:51:45 2020

@author: Roy
"""


'''
Create a class to represent a bank account.  It will need a to have a balance
and a method to withdraw, deposit money and display the balance
'''

class bank_account(object):
    
    def __init__(self, balance=0.0):
        self.balance = balance
        
    def display_balance(self):
        print(f'The balance of the account is {self.balance}')
        
    def deposit(self):
        amount = float(input('How much do you wish to deposit? >'))
        self.balance += amount
        print('Your deposit was successful, you now have a balance of £{self.balance}')
    
    def withdraw(self):
        amount = float(input('How much do you wish to withdraw? > '))
        self.balance -= amount
        print(f'Your new balance is {self.balance}')
        