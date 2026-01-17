n = int(input("Enter NUmber:"))
mulby2 = str(n * 2)
mulby3 = str(n * 3)
new = "".join(sorted(str(n)+mulby2+mulby3))
if new in "123456789":
    print("Fascinating Number")
else:
    print("Not Fascinating Number")