from math import *
n = int(input("Enter Limit:"))
count = 0

for num in range(2, n+1):
    is_prime = True

    for i in range(2, int(sqrt(num)+1)):
        if num%i == 0:
            is_prime = False
            break

    if is_prime:
        if count%2 == 0:
            print(num, end=" ")
        count += 1