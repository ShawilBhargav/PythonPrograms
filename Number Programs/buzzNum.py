n = (input("Enter Number:"))
if n[-1] == "7":
    print("Buzz Number")
elif int(n)%7 == 0:
    print("Buzz Number")
else:
    print("Not Buzz Number")