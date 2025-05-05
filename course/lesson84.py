import os
os.system('cls')

a, b = 1, 2
a, b = b, a

person = {
    'name': 'Filipe',
    'surname': 'Silva'
}

data_person = {
    'age': 38,
    'height': 1.73
}

completed_person = {**person, **data_person}
print(completed_person)

# a, b = person.items()
# print(a, b)

# (a1, a2), (b1, b2) = person.items()
# print(a1, a2)
# print(b1, b2)

# for key, value in person.items():
#     print(key, value)

def show_kwargs(*args, **kwargs):
    print('Not kwargs:', args)
    
    for key, value in kwargs.items():
        print(key, value)
        
# show_kwargs(name='Filipe', age=38)
show_kwargs(**completed_person)