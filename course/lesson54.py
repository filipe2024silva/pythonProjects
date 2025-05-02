import os

list = []

while True:
    print('Select an option')
    option = input('[i]Insert [d]delete [l]list: ')
    
    if option == 'i':
        os.system('cls')
        value = input('Type value: ')
        list.append(value)
    elif option == 'd':
        value = input('Type index value: ')
        try:
            index = int(value)
            del list[index]
        except ValueError:
            print('The index must have an integer number')
        except IndexError:
            print('The list is empty')
        except Exception as e:
            print(e)
    elif option == 'l':
        os.system('cls')
        if len(list) == 0:
            print('The list is empty')
        for i, value in enumerate(list):
            print(i, value)
    else:
        print('Please, type i, d or l')
    
    