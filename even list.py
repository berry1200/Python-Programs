l=[1,3,9,4,15,9,28,6,9,5,11]
print(l)
l.sort()
for i in l:
  if i%2==0:
    print("even no is :",i)
  elif i%2==1:
    print("odd no is : ",i)