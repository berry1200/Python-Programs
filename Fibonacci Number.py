def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n
n = int(input("enter a number : "))
if is_fibonacci(n):
   print("Fibonacci Number")
else:
    print("Not a Fibonacci Number")