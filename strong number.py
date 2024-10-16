import math
def is_strong_number(n):
    num_str = str(n)
    factorial_sum = sum(math.factorial(int(digit)) for digit in num_str)
    return factorial_sum == n

a = int(input("Enter a number: "))
if is_strong_number(a):
    print("Strong Number")
else:
    print("Not a Strong Number")