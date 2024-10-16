def is_polydivisible(n):
    num_str = str(n)
    for i in range(1, len(num_str) + 1):
        prefix = int(num_str[:i])
        if prefix % i != 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_polydivisible(num):
    print("Polydivisible Number")
else:
    print("Not a Polydivisible Number")

