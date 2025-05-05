import os

os.system('cls')

person = {}

key = 'name'

person[key] = 'Filipe Silva'
person['surname'] = 'Silva'

print(person)
print(person['name'])

del person['surname']

if person.get('surname') is None:
    print("The key is not valid")
else:
    print(person['surname'])

print(person)