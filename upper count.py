text = str(input("Enter a String  "  ))
upper=0
lower=0
for i in text:
    if(i.islower()):
        lower+=1
    else:
        upper+=1
print("number of lower : ",lower)
print("number of upper : ",upper)