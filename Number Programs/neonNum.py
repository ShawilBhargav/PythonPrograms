'''
Sum of digits of square of number = number.
'''

n = int(input("Enter Number:"))
sqnum = n**2
temp = sqnum
sum = 0
while temp > 0:
    digit = temp%10
    sum += digit
    temp //= 10

if sum == n:
    print("Neon Number")
else:
    print("Not Neon Number")