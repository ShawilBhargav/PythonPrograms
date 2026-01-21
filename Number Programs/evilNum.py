n = int(input("Enter Number:"))
binary = bin(n)[2:]
lisbin = list(map(int, binary))
count = lisbin.count(1)
if count % 2 == 0:
    print("Evil Number")
else:
    print("Not Evil Number")