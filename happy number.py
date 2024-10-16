def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

num = int(input("Enter a number: "))
if is_happy(num):
    print("Happy Number")
else:
    print("Not a Happy Number")

    ''' 1, 7, 13, 19, 23, 28, 44, 49, 68, 79, 129, 133, 139, 167, 188, 226, 236'''