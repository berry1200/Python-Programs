print(" Roadtax Calculator")
cost = float(input("price of the bike:  "))
if cost >100000:
    print("tax :",cost*(15/100))
elif cost >50000 and cost <=100000:
       print("tax :",cost*(10/100))
elif cost <= 50000:
           print("tax :",cost*(5/100))