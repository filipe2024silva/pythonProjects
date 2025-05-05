import os
os.system('cls')

def execute(function, *args):
    return function(*args)

print(execute(lambda x, y: x + y, 2, 3))

double = execute(lambda m: lambda n: n * m, 2)
print(double(3))