import math
n=371
sum=0
t=n
while n>0:
    r=math.floor(n%10)
    sum=sum+(r*r*r)
    n=n/10
if sum==t:
    print("armstrong")
else:
    print("not")