#Find the factorial of number<20
#and also number>20


#For number<=20
def fact(x):
  if x==0:
    return 1
  else:
    return x*fact(x-1)
    
    
#For number >=20
i=int(input())
fact=1
for j in range(i,-1,-1):
  if j!=0:
     fact=fact*j
  else:
     fact=fact*1
  
  
    
