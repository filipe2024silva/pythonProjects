print("Hello world")

#Types of variables
name = "Filipe"
age = 38
height = 1.73
developer = True

print(name, age, height, developer)

#operators
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 (divisão inteira)
print(a % b)   # 1 (resto)
print(a ** b)  # 1000 (potência)

#Conditionals
age = 18

if age >= 18:
    print("Major age!")
else:
    print("Minor age!")
    
#Cycles
for i in range(5):
    print("Value of i: ", i)

counter = 0

while counter < 5:
    print("Counting:", counter)
    counter += 1