import math
n=int(input("enter n:"))
rev=0
while n>0:
    a=math.floor(n%10)
    rev=rev*10+a
    n=n/10
print(rev)    

    
