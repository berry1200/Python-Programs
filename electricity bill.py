def calculate_electricity_bill(units):
    """
    Calculates the electricity bill based on the number of units used.

    """
    if units <= 100:
        return 0
    elif units <= 200:
        return (units - 100) * 5
    else:
        return (100 * 5) + (units - 200) * 10

def main():
    units = int(input("Enter the number of units used: "))
    bill = calculate_electricity_bill(units)
    print(f"Your electricity bill is: Rs. {bill}")

if __name__ == "__main__":
    main()