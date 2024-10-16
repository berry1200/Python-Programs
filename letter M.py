for i in range(1,8):
    for j in range(1,6):
        if (j==1 or j==5 or (i==2 and j!=3) or (i==3 and j!=2 and j!=4)) :
            print("*",end="  ")
        else:
            print(end="   ")
    print() 