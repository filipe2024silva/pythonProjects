import os
os.system('cls')

list = [4, 32, 1, 34, 5, 6, 6, 21]
list2 = [
    {'name': 'Filipe', 'surname': 'Silva'},
    {'name': 'Manuel', 'surname': 'Silva'},
    {'name': 'Pedro', 'surname': 'Silva'},
    {'name': 'Catarina', 'surname': 'Silva'},
    {'name': 'Andrade', 'surname': 'Silva'},
    {'name': 'Paulo', 'surname': 'Silva'},
]

# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)

def show(list):
    for item in list:
        print(item)
    print()

l1 = sorted(list2, key = lambda item: item['name']) #create a new list like as copy
l2 = sorted(list2, key = lambda item: item['surname'])

show(l1)
show(l2)