'''
Same as Krishnamurthy number.
Different name, same logic.
'''

from math import factorial
n = int(input("Enter number:"))
temp = n
sum = 0
while temp > 0:
    dig = temp%10
    fact = factorial(dig)
    sum += fact
    temp = temp//10
if sum == n:
    print("Peterson")
else:
    print("Not Peterson")