n = input("enter a string:  ")
word = sum(1 for char in n[:4] if char.isupper())
if word >= 2:
    print(n.upper())
else:
    print(n)