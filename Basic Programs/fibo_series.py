def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("Enter number:"))
ans = fibo(num)
print(f"Fibonacci of {num} is {ans}")