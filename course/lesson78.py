import os
import copy
os.system('cls')

d1 = {
    'c1':1,
    'c2':2,
    'l1':[1, 2, 3]
}

d2 = d1.copy()  
d3 = copy.deepcopy(d1)

d1['c1'] = 300
d1['l1'][0] = 500

print(d2)
print(d3)
d3['l1'][0] = 69
print(d3)