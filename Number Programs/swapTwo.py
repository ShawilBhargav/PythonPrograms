a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))
print(f"Before Swapping: a={a}, b={b}")
a = a^b
b = a^b
a = a^b
print(f"Before Swapping: a={a}, b={b}")