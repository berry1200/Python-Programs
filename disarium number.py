def is_disarium(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** (i + 1) for i, digit in enumerate(num_str))
    return sum_of_powers == n

num = int(input("Enter a number: "))
if is_disarium(num):
    print("Disarium Number")
else:
    print("Not a Disarium Number")

    ''' 89, 135, 518 etc. To find whether given number is Disarium or not, 
    calculate the sum of digits powered with their respective positions. 
    If the sum is equal to the original number then, the given number is Disarium number.'''