# def prime_num(n):
#     for i in range(2,n):
#         if n%i==0:
#           print("Not Prime")
#           return
#     print("Prime")

n = int(input("Enter number:"))
# prime_num(n)

from math import *
for i in range(2, int(sqrt(n))+1):
    if n%i==0:
        print("Not Prime")
else:
    print("Prime")