def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_fibonacci(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return True
    else:
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n

def is_fibonacci_palindrome(n):
    return is_palindrome(n) and is_fibonacci(n)

num = int(input("Enter a number: "))
if is_fibonacci_palindrome(num):
    print("Fibonacci Palindrome")
else:
    print("Not a Fibonacci Palindrome")

    '''  If you consider the Fibonacci sequence (each number is the sum of the two preceding ones:
    0, 1, 1, 2, 3, 5, 8, 13, 21, ...), you can find palindromic patterns within it. For example, 121 and 131 '''