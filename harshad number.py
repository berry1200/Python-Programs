def is_harshad(n):
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0

num = int(input("Enter a number: "))
if is_harshad(num):
    print("Harshad Number")
else:
    print("Not a Harshad Number")
""" The number 18 is a harshad number in base 10,
 because the sum of the digits 1 and 8 is 9, and 18 is divisible by 9. 
 The Hardy–Ramanujan number (1729) is a harshad number in base 10,
   since it is divisible by 19, the sum of its digits (1729 = 19 × 91). """