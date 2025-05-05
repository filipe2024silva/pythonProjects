import os
os.system('cls')

def sum_numbers(*args):#args packaging the arguments
    total = 0
    for number in args:
        total += number
    return total
    
    print(total)
numbers = 1, 2, 3, 4, 5, 6, 7, 78, 10
other_sum = sum_numbers(*numbers)
print(other_sum)

print(sum(numbers))
#sum_numbers(1, 2, 3, 4, 5, 6)
#print(sum((1, 2, 3, 4, 5, 6)))