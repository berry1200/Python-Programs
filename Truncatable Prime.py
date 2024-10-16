def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    num_str = str(n)
    for i in range(1, len(num_str)):
        left_trunc = int(num_str[i:])
        right_trunc = int(num_str[:-i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

num = int(input("Enter a number: "))
if is_truncatable_prime(num):
    print("Truncatable Prime")
else:
    print("Not a Truncatable Prime")
    
    '''239 is right-truncatable prime since 239, 23 and 2 are all prime '''