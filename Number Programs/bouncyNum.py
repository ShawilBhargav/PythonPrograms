'''
Digits go up and down randomly.
Not fully increasing, not fully decreasing.
EXAMPLE: 155349
'''

n = (input("Enter Number:"))
mapped = list(map(int, n))
print(mapped)
temp = list(map(int,sorted(n)))
print(temp)
if int(n) < 100:
    print("Not Bouncy Number")
elif mapped == temp:
    print("Not Bouncy Number")
else:
    print("Bouncy Number")