import os
os.system('cls')

person = {
    'name': 'Filipe',
    'surname': 'Silva'
}

#print(person.get('name'))

# name = person.pop('name')
# print(name)
# print(person)

last_key = person.popitem()#delete last key of the dictionary
print(last_key)
print(person)

#person.update(name='Pedro', age=38) 
#person.update({'name': 'Pedro', 'age': 38})
tuple = (('name', 'Pedro'), ('age', 38)) #tuple = ('name', 'Pedro'), #the comma must be in tuple end if i have just one item
person.update(tuple)

list = [['name', 'Catarina'], ['age', 2]]
person.update(list)

print(person)