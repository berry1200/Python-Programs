a = float(input("enter the height in meter :"))
b = int(input("enter the weight in kg"))
c = b/(a**2)
if c<18.5:
    print("they are under weight ")
elif c>18.5 and c<30:
    print("they hav ea normal weight")
elif c>25 and c<30:
     print("slight over weight")
elif c>30 and c<35:
    print("obese")
else:
    print("clinical obese")
