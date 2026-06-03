'''
Newton-Raphson Method to find root
Formula:
next_guess = (curr_guess + num/curr_guess)/2
'''
def sqr_root(num, decimal=6):
        # 1. Initial guess
        guess = num / 2.0

        # 2. Threshold for accuracy
        tolerance = 10 ** -(decimal+2)

        while True:
            # 3. Formula
            better_guess = 0.5 * (guess + (num/guess))

            # 4. Stopping loop
            if abs(guess - better_guess) < tolerance:
                return round(better_guess, decimal)

            guess = better_guess

n = int(input("Enter Number:"))
if n < 0:
    print("Root of -ve number is imaginary")
elif n == 0:
    print("Root of 0 is 0")
else:
    sq_root = sqr_root(n)
    print(f"Square root of {n} is {sq_root}")