'''
A number that is the product of exactly three different prime numbers.
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
# print(factors)
if len(factors) == len(set(factors)):
    print("Sphenic Number")
else:
    print("Not Sphenic Number")