list_1 = []
list_2 = [123, True, 'Filipe', 3.3]
list_3 = [10, 20, 30]
list_4 = [40, 50, 60]
list_5 = list_3 + list_4

#print(list_2, type(list_2))
print(list_2)
#print(bool(list_2))

del list_2[2] #index -1 always is the index of last item of list
print(list_2)

list_1 = list_2#when is changed some value in list_2 the list_1 is affected
print(list_1)

list_1 = list_2.copy()#the list_1 is not affected when to change some value in list_2

list_2.append(50)
print(list_2)
print(list_1)

number_removed = list_2.pop()
print(list_2, 'Removed', number_removed)

number_removed = list_2.pop(0)
print(list_2, 'Removed', number_removed)

list_2.insert(1, 'Filipe')
print(list_2)

print(list_5)

list_2.extend(list_5)
print(list_2)

list_1 = list_2
print(list_1)