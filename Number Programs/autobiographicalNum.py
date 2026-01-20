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