import math
n=5436
sum=0

while n>0:
    r=math.floor(n%10)
    sum=sum*10+r
    n=n/10
print(sum)