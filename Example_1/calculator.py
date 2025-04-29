def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a,b):
    return a * b

def divide(a, b):
    return a / b

print("Select operation: +, -, *, /")

operation = input("Operation: ")
x=float(input("Type first digit: "))
y=float(input("Type second digit: "))

if operation == "+":
    print("Result: ", sum(x, y))
elif operation == "-":
    print("Result: ", sub(x, y))
elif operation == "*":
    print("Result: ", multi(x, y))
elif operation == "/":
    print("Result: ", divide(x, y))
else:
    print("Operation invalid!")