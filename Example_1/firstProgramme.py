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
    
#functions
def welcome(name):
    print("Welcome", name)
    
welcome("Filipe")

#List, dictionaries, tuple
#Lists
fruits = ["apple", "banana", "grape"]
print(fruits[0]) #apple
print(fruits)
fruits.append("orange")
print(fruits)

#Dictionary
person = {"name": "Ana", "age": 30}
print(person["name"]) #Ana

#Tuple
coordenates = (10, 20)
print(coordenates[1]) #20

#Entry of data
name = input("Type your name: ")
print("Hello", name)

def maca():
    return "Você escolheu maçã."

def banana():
    return "Você escolheu banana."

def uva():
    return "Você escolheu uva."

#"switch" using dictionary
options = {
    "1": maca,
    "2": banana,
    "3": uva
}

opcao = input("Escolha uma fruta (1- maçã, 2- banana, 3- uva): ")
acao = options.get(opcao, lambda: "Opção inválida.")
print(acao())

#Strings
name = " Filipe Silva"
print(name.strip().upper())

#Errors
try:
    number = int(input("Digite um número: "))
    print(10 / number)
except ValueError:
    print("You digited no number")
except ZeroDivisionError:
    print("You can`t to divide for zero")
    
#Read and write files
with open("file.txt", "w") as f:
    f.write("Olá, Filipe!")

with open("file.txt", "r") as f:
    print(f.read())