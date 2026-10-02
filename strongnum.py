import math
n=int(input("enter n:"))
t=n
sum=0
while n>0:
    r=math.floor(n%10)

    fact=1
    i=1

    while i<=r:
        fact=fact*i
        i+=1

    sum+=fact
    n=math.floor(n/10)

if sum==t:
    print("strong number")
else:
    print("not")
