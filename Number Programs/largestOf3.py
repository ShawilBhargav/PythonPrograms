a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
if a>b:
    if a>c:
        print("A is largest")
    else:
        print("C is largest")
elif b>c:
    print("B is largest")
else:
    print("C is largest")