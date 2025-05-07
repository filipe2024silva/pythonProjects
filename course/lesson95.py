import os
os.system('cls')

try:
    a = 18
    b = 0
    print('Line 1'[1000])
    c = a / b
    print('Line 2')
except ZeroDivisionError:
    print('Divide for zero')
except NameError:
    print('Name b not defined')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Name:', error.__class__.__name__)
except Exception:
    print("Unknown error")
