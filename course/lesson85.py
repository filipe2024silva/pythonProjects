#list comprehension is a quick way to create lists from iterables

import os
os.system('cls')

print(list(range(10)))

list = [number * 2 for number in range(10)]
print(list)