import os

os.system('cls')

def sum(x, y):
    return x + y

def multi(x, y):
    return x * y

def execute(function, x):
    def internal(y):
        return function(x, y)
    return internal

sum_func = execute(sum, 5)
multi_func = execute(multi, 5)

print(sum_func(3))
print(multi_func(2))