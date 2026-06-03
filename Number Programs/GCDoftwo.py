a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
while b != 0:
    # a, b = b, a % b
    rem = a%b
    a = b
    b = rem

print(f"GCD of two number is: {a}")