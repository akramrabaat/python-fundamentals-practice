
password = input("Enter your password: ")

has_upper = False
has_lower = False
has_number = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_number = True

if len(password) < 6:
    print("Weak Password")
elif len(password) >= 8 and has_upper and has_lower and has_number:
    print("Strong Password")
else:
    print("Moderate Password")