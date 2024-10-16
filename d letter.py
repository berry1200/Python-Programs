for i in range(1,8):
    for j in range(1,6):
        if(j==1 or (i==1 and j!=1) or i==7 or (j==5)):
            print("*",end=" ")
        else:
            print(end="   ")
    print() 