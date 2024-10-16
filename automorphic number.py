num = int(input("Enter a number: "))
def is_automorphic(n):
    square = str(n ** 2)
    return square.endswith(str(n))
if is_automorphic(num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number") 
    
''' (25)2 = 625, and (76)2 = 5776. '''