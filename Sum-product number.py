def is_sum_product_number(n):
    digits = [int(d) for d in str(n)]
    digit_sum = sum(digits)
    digit_product = 1
    for digit in digits:
        digit_product *= digit
    return digit_sum == digit_product

num = int(input("Enter a number: "))
if is_sum_product_number(num):
    print("Sum-product Number")
else:
    print("Not a Sum-product Number")

    '''  There are only three sum-product numbers: 1, 135, and 144 '''