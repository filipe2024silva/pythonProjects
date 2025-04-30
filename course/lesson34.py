condition = True

"""
while condition:
    name = input('Type your name: ')
    print(f'your name is {name}')
    
    if name == 'out':
        break
"""
while True:
    out = input('Do you want exit? [e]xit: ').lower().startswith('e')
    
    if out:
        break

print("Finished")

#break e continue used with the nearest condition 