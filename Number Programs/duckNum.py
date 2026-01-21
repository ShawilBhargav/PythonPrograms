n = int(input("Enter Number:"))
if n < 0:
    print("Not Duck Number")
elif "0" in str(n) and str(n)[0] != 0:
    print("Duck Number")
else:
    print("Not Duck Number")