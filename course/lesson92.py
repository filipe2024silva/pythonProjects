#generator expression, iterables and iteretaors
import os
import sys

os.system('cls')

iterable = ['I', 'have', '__iter__']
iterator = iter(iterable) #__iter__() and __next__
list = [n for n in range(10000)]
generator = (n for n in range(10000))#just is possible read values sequentially

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

print(sys.getsizeof(list))
print(sys.getsizeof(generator))