# 1. Variables, Comments, Print
name = "Rabat"  # variable
age = 22
print(name, age)

# 2. Input and Type Casting
n = int(input("Enter number: "))
x = float("2.5")
print(n, x)

# 3. Operators
a, b = 10, 5
print(a + b, a - b, a * b, a / b)  # arithmetic
print(a > b, a == b, a != b)       # comparison
print(a > 0 and b > 0)             # logical
a += 2                             # assignment
print(a)

# 4. If, If-Else, If-Elif
if n > 0:
    print("Positive")

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

if n > 0:
    print("Positive")
elif n == 0:
    print("Zero")
else:
    print("Negative")

# 5. While Loop
i = 1
while i <= 3:
    print(i)
    i += 1

# 6. For, Break, Continue, Else
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

for i in range(3):
    print(i)
else:
    print("Done")

# 7. Functions
def add(a, b):
    return a + b

print(add(2, 3))

# 8. Variable Scope
x = 10  # global

def show():
    y = 5  # local
    print(x, y)

show()

# 9. List
L = [1, 2, 3]
L.append(4)
print(L, L[0])

# 10. Tuple
T = (1, 2, 3)
print(T, T[0])

# 11. Set
S = {1, 2, 2, 3}
S.add(4)
print(S)

# 12. Dictionary
D = {"name": "Ali", "age": 20}
D["age"] = 21
print(D, D["name"])

# 13. Strings: Indexing and Slicing
s = "Python"
print(s[0])       # indexing
print(s[1:4])     # slicing
print(s[-1])      # last character
print(s[::-1])    # reverse
