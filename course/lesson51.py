#Tuples introduction
names_list = ['Filipe', 'João', 'Manuel'] 

#name_1, name_2, name_3 = names_list #OR name_1, name_2, name_3 = ['Filipe', 'João', 'Manuel'] 

#name_1, *_ = ['Filipe', 'João', 'Manuel'] 
#_, name_2, *_ = ['Filipe', 'João', 'Manuel'] 
#print(name_1)
#print(name_2)

enum_list = list(enumerate(names_list))
#print(next(enum_list))

print(enum_list)

for item in enum_list:
    print(item)