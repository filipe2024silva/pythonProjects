#Higher Order Functions

def message(msg, name):
    return f'{msg}, {name}'

def execute(function, *args):
    return function(*args)

print(execute(message, 'Good morning'))