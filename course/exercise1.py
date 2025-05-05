import os
os.system('cls')

name = input("Type your name: ")
age = input("Type your age: ")

if name and age:
    print(f'Your name is {name}')
    print(f'Your name inverted is {name[::-1]}')
    if ' ' in name:
        print(f'Your name have spaces')
    else:
        print("Your name haven`t spaces")
    print(f'Your name have {len(name)} characteres')
    print(f'The first character in your name is {name[0]}')
    print(f'The last character in your name is {name[len(name) - 1]}')
else:
    print('Sorry, the fields are empty')