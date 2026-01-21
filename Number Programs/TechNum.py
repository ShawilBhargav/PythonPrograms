'''
Split number into two equal parts, add them, square the sum.
'''

n = int(input("Enter Number:"))
if len(str(n))%2 != 0:
    print("Not Tech Number")
else:
    fpart = n // 100
    spart = n % 100
    sum = fpart + spart
    if sum**2 == n:
        print("Tech Number")
    else:
        print("Not Tech Number")