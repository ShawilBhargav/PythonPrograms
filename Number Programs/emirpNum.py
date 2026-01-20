from math import *
def primenum(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True

n = int(input("Enter Number:"))
temp = n
rev = 0
while temp > 0:
    digit = temp%10
    rev = (rev*10) + digit
    temp //= 10

if primenum(n) == primenum(rev):
    print("Emirp Number")
else:
    print("Not Emirp Number")