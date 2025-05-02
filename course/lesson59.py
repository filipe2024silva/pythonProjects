string= 'ABCD'
list = ['Filipe', 'Helena', 1, 2, 3, 'Quim']
tuple = 'Python is cool'
rooms = [['Maria', 'Helena', ], ['João', ], ['Filipe', 'Pedro', 'Manuel',],]

print(*list)
print(*string)
print(*tuple)
print(*rooms, sep='\n')