n = int(input("Enter no: of Rows: ")) 
for i in range(n,-1,-1): 
    for j in range(i,0,-1):  
        print("*", end=" ")
    for j in range(2*(n-i)): 
        print( end="  ")
    for j in range(i,0,-1):  
        print("*", end=" ")
    print()
for i in range(1,n+1): 
    for j in range(1,i+1):
        print("*", end=" ")
    for j in range(2*(n-i)):
        print(end="  ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()