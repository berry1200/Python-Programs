for i in range(1,8):
    for j in range(1,6):
        if((i==1 and j!=5) or i==4 or j==1 or (i==7 and j!=5) or(j==5 and i!=1 and i!=7)):
            print("*",end=" ")
        else:
            print(end="  ")
    print() 