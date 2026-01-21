'''
Recursive program to reverse a number
'''
def revnum(n):
    if len(n) <= 1:
        return n
    else:
        return revnum(n[1:]) + n[0]

num = input("Enter Number:")
ans = revnum(num)
print(f"Reverse of {num} is {ans}")