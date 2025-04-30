name = input("What`s your name? ")
print(f"Your name is {name}")
print(f"Your name is {name = }")

entry = input(f'{name}, do you want enter in system? Type "Yes" or "No": ')

if entry == 'Yes':
    print("You are inside the System")
elif entry == 'No':
    print("System stay closed")
else:
    print("Incorrect command")