for i in range(1,8):
    for j in range(1,7):
        if((i==1 and j!=1) or (j==1 and i!=1 and i!=7) or (i==7 and j!=1 and j!=5) or (j==6 and i!=2 and i!=3) or (j==4 and i!=2 and i!=3) or (i==4 and j!=2 and j!=3)):
            print("*",end="  ")
        else:
            print(end="   ")
    print() 