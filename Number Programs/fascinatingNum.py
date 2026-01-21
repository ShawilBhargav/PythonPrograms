'''
Multiply number by 2 and 3, join all results.
If digits 1 to 9 appear exactly once, it’s fascinating.
'''

n = int(input("Enter Number:"))
mulby2 = str(n * 2)
mulby3 = str(n * 3)
new = "".join(sorted(str(n)+mulby2+mulby3))
if new in "123456789":
    print("Fascinating Number")
else:
    print("Not Fascinating Number")