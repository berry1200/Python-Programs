""" First few strong prime numbers are 11, 17, 29, 37, 41, 59, 67, 71, """
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_nearest_primes(n):
    lower = n - 1
    while not is_prime(lower):
        lower -= 1
    upper = n + 1
    while not is_prime(upper):
        upper += 1
    return lower, upper

def is_strong_prime(n):
    if not is_prime(n):
        return False
    lower, upper = find_nearest_primes(n)
    mean = (lower + upper) / 2
    return n > mean

num = int(input("Enter a number: "))
if is_strong_prime(num):
    print("Strong Prime")
else:
    print("Not a Strong Prime")