'''
A number that describes itself.
Index tells how many times a digit appears.
EXAMPLE: 1210
0 appears 1 time, 1 -> 2, 2 -> 1,  3 -> 0
'''

n = (input("Enter Number:"))
digit = list(map(int, n))
print(digit)
flag = True
for i in range(len(digit)):
    if digit[i] != digit.count(i):
        flag = False
        break

if flag:
    print("Autobiographic Number")
else:
    print("Not Autobiographic Number")