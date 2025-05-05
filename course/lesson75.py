#Dictionary
import os
os.system('cls')

#person = dict(firstname='Filipe', lastname='Silva') #used to create dictionary but not used frequently

person = {
    'firstname': 'Filipe',
    'lastname': 'Silva',
    'age': 18,
    'height': 1.73,
    'addresses':[
        {'street': 'street House', 'number': 168},
        {'street': 'street Hotel', 'number': 125}
    ]
}


print(type(person))
print(person)
print(person['firstname'])
print(person['addresses'][0])

for key in person:
    print(key, person[key])