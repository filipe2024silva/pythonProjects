import os
os.system('cls')

# def generator(n=0):
#     yield 1 #Pause
#     print('Continue...')
#     yield 2
#     print('Continue...')
#     yield 3
#     print('Continue...')
#     yield 4

def generator(n=0, maximum=10):
    while True:
        yield n
        if n >= maximum:
            return
        n += 1
        
    
gen = generator(0)
# print(next(gen))    
# print(next(gen))    
# print(next(gen)) 
# print(next(gen)) 
# print(next(gen)) 

for n in gen:
    print(n)