#dir, hasattr and getattr
import os
os.system('cls')

string = 'Filipe'
method = 'upper'

if hasattr(string, method):
    print('Exist Upper')
    print(getattr(string, method)())
else:
    print('Not exist method', method)