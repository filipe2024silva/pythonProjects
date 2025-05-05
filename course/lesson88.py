#Dictionary Comprehension and Set Comprehension

import os
os.system('cls')

product = {
    'name': 'Blue Pen',
    'price': 2.5,
    'category': 'Office'
}

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in product.items()
    if key != 'category'
}

print(dc)