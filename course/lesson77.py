import os
os.system('cls')

person = {
    'name': 'Filipe',
    'surname': 'Silva'
}

#print(len(person))
#print(person.keys())
#tuple_person = tuple(person.values())
#print(tuple_person)
#print(tuple_person[0])
#list_person = list(person.values())
#print(list_person)
#print(list_person[0])
#print(list(person.items()))

person.setdefault('age', None)# add a new key if not exist
print(person['age'])