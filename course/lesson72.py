import os
os.system('cls')

def multi(*args):
    total = 1
    for number in args:
         total *= number
    return total

variable = multi(1,2,3,4,5)

print(variable)