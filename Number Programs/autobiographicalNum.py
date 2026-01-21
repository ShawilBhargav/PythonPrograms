'''
A number that describes itself.
Each digit tells how many times a digit appears.
'''

n = (input("Enter Number:"))
digit = list(map(int, n))
# print(digit)
flag = True
for i in range(len(digit)):
    if digit[i] != digit.count(i):
        flag = False
        break

if flag:
    print("Autobiographic Number")
else:
    print("Not Autobiographic Number")