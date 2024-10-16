a = int(input("ENTER A LIMIT")) 
sum=0
for i in range(0,a+1,1):
    if i%2!=0:
        sum=sum+i
print(sum)
if sum%2==0:
    print("sum s even number")
else:
    print("sum is odd number")