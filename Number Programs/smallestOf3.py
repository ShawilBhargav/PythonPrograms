# SMALLEST AMONG 3 USING TERNARY OPERATOR
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

small = a if a<b else b
smallest = c if c<small else small
# smallest = a if a<b and a<c else (b if b<c else c)

print(f"Smallest among three number is {smallest}")