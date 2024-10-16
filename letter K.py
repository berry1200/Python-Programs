for i in range(1,8):
    for j in range(1,6):
        if j==1 or (i==4 and j!=3 and j!=4 and j!=5) or (j==3 and i!=1 and i!=2 and i!=4 and i!=6 and i!=7) or (j==4 and i!=1 and i!=3 and i!=4 and i!=5 and i!=7) or (j==5 and i!=2 and i!=3 and i!=4 and i!=5 and i!=6) :
            print("*",end="  ")
        else:
            print(end="   ")
    print() 