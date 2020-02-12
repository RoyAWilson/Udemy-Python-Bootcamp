# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:25:01 2020

@author: Roy
"""


class BankAccount(object):
#    ''' Docstring to go here'''
    
    def __init__(self,balance=0.0):
        self.balance = balance
        
    def display_balance(self):
        print(f'Your balance is {self.balance}')
        
    def make_deposit(self):
        amount = float(input('How much would you like to deposit?:> '))
        self.balance += amount
        print(f'Balance is now {self.balance}.')
        
    def make_withdrawal(self):
        amount = float(input('How much would you like to withdraw?:> '))
        if amount > self.balance:
            print(f'You do not have sufficient funds, your balance is {self.balance}')
        else:
            self.balance -= amount
            print(f'Withdrawal successful: balance is now {self.balance}.')