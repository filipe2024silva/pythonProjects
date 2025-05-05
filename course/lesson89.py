#isinstance -> for know if what is object type
import os
os.system('cls')

list = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'name': 'Filipe'},
]

for item in list:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print('STR')
        print(item.upper())

    if isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)