for i in range(1,9):
    for j in range(1,8):
        if((i==1 and j!=1 and j!=7) or (j==4 and i!=7 and i!=8) or (i==7 and j!=1 and j!=2 and j!=4 and j!=5 and j!=6 and j!=7) or (i==8 and j!=1 and j!=3 and j!=4 and j!=5 and j!=6 and j!=7) or (i==7 and j!=3 and j!=2 and j!=4 and j!=5 and j!=6 and j!=7)):
            print("*",end="  ")
        else:
            print(end="   ")
    print() 