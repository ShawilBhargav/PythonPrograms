'''
A number whose square ends with the same number.
EXAMPLE: 25
'''

n = int(input("Enter Number:"))
base = 10**len(str(n))
sq = n**2
if sq%base == n:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")