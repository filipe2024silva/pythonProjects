import os

os.system('cls')

def decorate(func):
    print('Decorator 1')

    def internal(*args, **kwargs):
        print('Nested')
        res = func(*args, **kwargs)
        return res
    return internal

@decorate
def sum(x, y):
    return x + y

example = sum(10, 5)
print(example)