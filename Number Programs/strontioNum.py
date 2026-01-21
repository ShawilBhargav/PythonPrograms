'''
A four-digit number that, when multiplied by 2,
results in a product where the digits in the hundreds and tens places are identical.
'''
n = int(input("Enter Number:"))*2
digit = list(map(int, str(n)))

if 1000 > n > 9999:
    print("Not Strontio Number")
elif digit[-2] == digit[-3]:
    print("Strontio Number")
else:
    print("Not Strontio Number")