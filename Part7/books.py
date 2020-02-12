# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 19:58:46 2019

@author: Roy
"""


books = {'Jingo':{'Author':'Terry Pratchett','Genre':'Fantasy'},'Quantum':{'Author':'Manjit Kumar','Genre':'Science Fact'},\
         'A Column of Fire':{'Author':'Ken Follett','Genre':'Historic Novel'},\
             'snuff':{'Author':'Terry Pratchett','Genre':'Fantasy'},'Tombland':{'Author':'C.J Sansom','Genre':'Historic Novel'}}
fndbk = input('Please enter a title to see the details (type \'x\' to finish) :> ')
if fndbk.lower() == 'x':
    print('goodbye!')
else:
    while fndbk not in books:
        print('Sorry I do not have that book is not available')
        fndbk = input('Please enter the the title to see the details :>')
    print(f'The following are the details for {fndbk}:  {books[fndbk]}')
