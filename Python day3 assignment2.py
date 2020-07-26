flag=0
n=eval(input("Enter a number"))
for i in range(2,int(n/2)):
    if(n%i==0):
      flag=1
      break
    else:
      flag=0
if(flag==0):
  print("prime")
else:
  print("not prime")