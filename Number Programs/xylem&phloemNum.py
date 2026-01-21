'''
Xylem Number if the sum of its extreme digits (first and last) is equal to the sum of its mean digits (all digits in between).
Phloem Number if the sum of its extreme digits is not equal to the sum of its mean digits.
'''

n = input("Enter Number:")
extreme_sum = int(n[0]) + int(n[-1])
mean_sum = 0
for i in range(1, len(n)-1):
    mean_sum += int(n[i])

print("Xylem Number" if mean_sum == extreme_sum else "Phloem Number")