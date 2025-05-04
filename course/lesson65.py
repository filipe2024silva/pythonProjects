#functions

global x #x is defined as global variable

def Print(a, b, c):
    print(a)
    print(b)
    print(c)

Print(1, 2, 3)

def sum(x, y):
    print(f'x = {x} y = {y}', '|', 'x + y =', x + y)
    return x + y

value = sum(1, 2)
print(value)
sum(2, 1)
sum(y=2, x=1)