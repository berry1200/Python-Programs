def is_palindrome(n):
    decimal_str = str(n)
    if decimal_str != decimal_str[::-1]:
        return False

    binary_str = bin(n)[2:]  
    if binary_str != binary_str[::-1]:
        return False

    return True

num = int(input("Enter a number: "))
if is_palindrome(num):
    print("The number is a palindrome in both decimal and binary representations.")
else:
    print("The number is not a palindrome in both decimal and binary representations.")