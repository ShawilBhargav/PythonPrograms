n = int(input("Enter Number:"))
temp = n
power = len(str(n))
sum = 0
while temp > 0:
    digit = temp % 10
    sq = digit**power
    sum += sq
    temp //= 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not")

