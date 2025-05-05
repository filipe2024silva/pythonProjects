import os
os.system('cls')

list = []

for x in range(3):
    for y in range(3):
        list.append((x, y))
        
list2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
        
print(list)
print(list2)