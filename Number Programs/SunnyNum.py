from math import sqrt
n = int(input("Enter Number:"))
new = n + 1
sqroot = sqrt(new)
if int(sqroot**2) == new:
    print("Sunny Number")
else:
    print("Not Sunny Number")