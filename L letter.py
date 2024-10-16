for i in range(1,8):
    for j in range(1,6):
        if ((j==1 and i!=1 )or i==7) :
            print("*",end="  ")
        else:
            print(end="   ")
    print() 