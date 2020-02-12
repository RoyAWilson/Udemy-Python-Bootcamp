# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:24:13 2020

@author: Roy
"""


def encrypt(text, enc_key):
    new_text = ''
    for letters in text:
        encrypted = chr(int(ord(letters)) + enc_key)
        new_text = new_text + encrypted
    return new_text

def decrypt(text, enc_key):
    decryption = ''
    for letters in text:
        dec_text = chr(int(ord(letters))-enc_key)
        decryption = decryption + dec_text
    return decryption
def main():
    choice = ''
    choice = input('Do you want to Encrypt or Decrypt a message:  >')
    
    if choice =='E':
        text = input('Please enter text to encrypt:  > ')
        enc_key = int(input('Please enter an integer incryption key:  >'))
        print(f'Your encrypted message reads:\n{encrypt(text, enc_key)}')
    elif choice == 'D':
        text = input('Text to decrypt:  >')
        enc_key = int(input('Please enter the decryption key provided to you:  >'))
        print(f'Your decrypted message reads:\n{decrypt(text, enc_key)}')
    else:
        print('You did not enter a valid choice of decryption or Encryption')
main()
retry = input('Do you want to try again Y/N >')
if input == 'N':
    print('Goodbye!')
else:
    main()
