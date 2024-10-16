text = str(input("Enter a String  "  ))
upper=0
lower=0
symbol=0
for i in text:
    if(i.isalpha()):
        lower+=1
    elif i.isnumeric():
        upper+=1
    elif not i.isspace():
        symbol+=1
print("number of alphabet : ",lower)
print("number of number : ",upper)
print("number of symbol : ",symbol)

