def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] = factors.get(i, 0) + 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

num = int(input("Enter a number: "))
factors = prime_factors(num)
print("Prime factors and their counts:")
for factor, count in factors.items():
    print(f"{factor}^{count}", end=" * ")
print()

# Print the prime factors in the format 2^2 * 5^1
print("Prime factors in the format a^b * c^d * ...:")
factors_str = " * ".join(f"{factor}^{count}" for factor, count in factors.items())
print(factors_str)