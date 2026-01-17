def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*fact(n-1)

num = int(input("Enter number:"))
ans = fact(num)
print(f"Factorial of {num} is {ans}")