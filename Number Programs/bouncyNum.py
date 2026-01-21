n = (input("Enter Number:"))
mapped = list(map(int, n))
temp = sorted(n)
temp_map = list(map(int, temp))
if int(n) < 100:
    print("Not Bouncy Number")
elif mapped == temp_map:
    print("Not Bouncy Number")
else:
    print("Bouncy Number")