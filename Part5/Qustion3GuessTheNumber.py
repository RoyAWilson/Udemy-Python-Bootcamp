# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:10:57 2019

@author: Roy
"""

## create variable with number between 1 and 10 get input of integer and tell user if guessed right or wrong.

my_number = 5

guess = input('Guess the number - Type an integer between 1 and 10 inclusive >> ')

if guess.isdigit():
    guess = int(guess)
    if guess <1 or guess > 10:
        print(f'{guess} is out of range')
    elif guess < my_number:
       print(f'Sorry you guessed wrong. {guess} is too low, guess right to win!')
    elif guess > my_number:
        print(f'Sorry you guessed wrong, {guess} is too high, guess right to win!')
    else:
        print('You guessed right! You win')
else:
    print(f'{guess} is not an integer!')
