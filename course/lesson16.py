enter = input('[E]nter [O]ut: ')
password = input('Type your password: ') or 'without password'
print(password)

passwordPermited = '1234'

if (enter == 'E' or enter == 'e') and password == '1234':
    print("You can enter")
else:
    print("You out")
    
print(not True)