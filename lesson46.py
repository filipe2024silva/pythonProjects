for i in range(10):
    if i == 2:
        print('i is 2, continue...')
        continue
    
    if i == 8:
        print('i is 8, breaking...')
        break
    
    for j in range(1, 3):
        print(i, j)
else:
    print('For was completed with success') 