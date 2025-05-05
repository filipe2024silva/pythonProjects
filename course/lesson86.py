import os

os.system('cls')

products = [
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 10, },
    {'name': 'p3', 'price': 30, },
]

new_products = [
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 20 else {**product} #mapping
    for product in products
    if product['price'] > 10 #filtering
]

#print(new_products)
print(*new_products, sep='\n')

#list = [n for n in range(10) if n < 5]
