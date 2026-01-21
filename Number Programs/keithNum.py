'''
A number that appears in a somewhat fibonacci series made from its digits.
'''

n = int(input("Enter Number:"))
temp = n
digit = []
while temp > 0:
    digit.append(temp%10)
    temp //= 10
digit.reverse()
# print(sum(digit))
while 1:
    maxsum = 0
    maxsum = sum(digit)

    if maxsum == n:
        print("Keith Number")
        break
    if maxsum > n:
        print("Not Keith Number")
        break
    digit.pop(0)
    digit.append(maxsum)