for i in range(1,8):
    for j in range(1,8):
        if (j==1 and i!=1 and i!=7) or (i==1 and j!=1 and j!=7) or (i==7 and j!=1 and j!=7) or (j==7 and i!=1 and i!=7) :
            print("*",end="  ")
        else:
            print(end="   ")
    print() 