full_name = input("Enter your full name: ")

names = full_name.split()

first_name = names[0]
last_name = names[-1]

initials = first_name[0].upper() + ". " + last_name[0].upper() + "."

print("Initials:", initials)
print("Name in Uppercase:", full_name.upper())
print("Reversed Name:", full_name[::-1])