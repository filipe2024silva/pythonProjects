import os

os.system('cls')
# def out(x):
#     a = x
#     def inside():
#         print(inside.__code__.co_freevars)
#         return a
#     return inside

# inside1 = out(10)
# inside2 = out(20)

# print(inside1())
# print(inside2())

def concat(initial_string):
    value = initial_string

    def internal(concat_value):
        nonlocal value
        value += concat_value
        return value
    return internal

c = concat('a')
print(c('b'))
print(c('c'))
print(c('d'))