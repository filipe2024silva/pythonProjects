import os
os.system('cls')

# print(123)
# raise ValueError('Error')
# print(456)

def zero_error_treatment(d):
    if d == 0:
        raise ZeroDivisionError('Error divide for zero')
    return True

def type_error_treatment(n):
    type_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} must be float or int'
        )


def divide(n, d):
    type_error_treatment(n)
    type_error_treatment(d)
    zero_error_treatment(d)
    return n/d

print(divide(8, 0))