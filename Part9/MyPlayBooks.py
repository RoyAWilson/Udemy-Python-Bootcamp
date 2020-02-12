# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:26:05 2019

@author: Roy
"""


class books(object):
    status = 'Novel'
    def __init__(self, title, author, published_yr):
        self.title = title
        self.author = author
        self.published_yr = published_yr
    def get_details(self):
        print(f'details of the book are {self.title} by {self.author} printed in {self.published_yr}')
    
book = books('The Truth', 'Terry Pratchett', 2000)
book1 = books('A Column of Fire', 'Ken Follet', 2017)

print(book.title, book.author, book.published_yr, book.status)
print(book1.title, book1.author, book1.published_yr, book1.status)