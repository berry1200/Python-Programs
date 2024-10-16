import math

def is_perfect_square(n):
    sqrt = math.isqrt(n)
    return sqrt * sqrt == n

def is_squarefree(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % (i * i) == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_squarefree(num):
    print("Squarefree Number")
else:
    print("Not a Squarefree Number")

    ''' The number 1 is by convention taken to be squarefree.
    The squarefree numbers are 1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15 '''