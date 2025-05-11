import copy
import os
from data import products

new_products = [
    {**p, 'price': round(p['price'] * 1.1, 2)}
    for p in copy.deepcopy(products)
]

os.system('cls')

print(*products, sep='\n')
print()
print(*new_products, sep='\n')
print('---------------------------')

products_by_name = sorted(
    copy.deepcopy(products),
    key=lambda p: p['name'],
    reverse=True
)

print(*products, sep='\n')
print()
print(*products_by_name, sep='\n')
print('---------------------------')

products_by_price = sorted(
    copy.deepcopy(products),
    key=lambda p: p['price'],
    reverse=True
)

print(*products, sep='\n')
print()
print(*products_by_price, sep='\n')