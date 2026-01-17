n = int(input("Enter Number:"))
temp = n
sum = 0
prod = 1
while temp > 0:
    digit = temp % 10
    sum += digit
    prod *= digit
    temp //= 10

if sum == prod:
    print("Spy Number")
else:
    print("Not Spy Number")