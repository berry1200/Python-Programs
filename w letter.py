for i in range(1,7):
    for j in range(1,8):
        if (j==1 or j==7 or i==5 and j!=3 and j!=4 and j!=5 or i==4 and j!=2 and j!=4 and j!=6 or i==3 and j!=2 and j!=3 and j!=6 and j!=5) :
            print("*",end=" ")
        else:
            print(end="  ")
    print() 