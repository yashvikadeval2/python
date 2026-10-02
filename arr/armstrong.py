import math
n=int(input("enter n:"))
sum=0
x=n
while n>0:
    a=math.floor(n%10)
    sum=sum+(a*a*a)
    n=n/10
    
if x==sum:
    print("this number is armstrong")
else:
    print("this number is not armstrong")

