'''
Composite number whose:
Sum of digits = Sum of digits of its prime factors
'''

n = int(input("Enter Number:"))
temp = n
i = 2
factors = []
while i*i <= n:
    while temp % i == 0:
        factors.append(i)
        temp //= i
    i += 1
if temp > 1:
    factors.append(temp)

fac_sum = 0
for f in factors:
    while f > 0:
        fac_sum += f%10
        f //= 10

temp2 = n
dig_sum = 0
while temp2 > 0:
    digit = temp2 % 10
    dig_sum += digit
    temp2 //= 10

if fac_sum == dig_sum:
    print("Smith Number")
else:
    print("Not Smith Number")