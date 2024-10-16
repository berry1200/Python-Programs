for i in range(1,8):
    for j in range(1,6):
        if(j==1 or j==5 or i==4):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
