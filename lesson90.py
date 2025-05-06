import os
os.system('cls')

list = []
dictionary = {}
conj = set()
tuple = ()
string = ''
integer = 0
float_variable = 0.0
none_variable = None
false_variable = False
range_variable = range(0)

def falsy(value):
    return 'falsy' if not value else 'truthy'

print(f'TEST', falsy('TEST'))
print(f'{list=}', falsy(list))
print(f'{dictionary=}', falsy(dictionary))
print(f'{conj=}', falsy(conj))
print(f'{tuple=}', falsy(tuple))
print(f'{string=}', falsy(string))
print(f'{integer=}', falsy(integer))
print(f'{float_variable=}', falsy(float_variable))
print(f'{none_variable=}', falsy(none_variable))
print(f'{false_variable=}', falsy(false_variable))
print(f'{range_variable=}', falsy(range_variable))