#Sets
import os
os.system('cls')

# s1 = set('Filipe')
# s2 = {'Filipe', 1, 2 ,3}#just acept immutables values
# s3 = set()

# print(s1)
# print(s2)
# print(s3)

# s1 = {1, 2, 3, 3, 3, 1}
# print(s1)
# print(3 in s1)

# for number in s1:
#     print(number)

s1 = set()
s1.add('Filipe')
s1.add(1)
s1.update(('Hello world', 1, 2, 3, 4))
print(s1)

s1.discard('Hello world')

# s1.clear()
print(s1)