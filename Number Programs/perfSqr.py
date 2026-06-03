n = int(input("Enter Number: "))
low = 1
high = n
flag = False
while low <= high:
    mid = (low+high)//2

    if mid**2 == n:
        flag = True
        break
    elif mid**2 > n:
        high = mid - 1
    else:
        low = mid + 1

if flag:
    print("Perfect Square Number")
else:
    print("Not Perfect Square Number")