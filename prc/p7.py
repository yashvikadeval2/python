import math
n=76543
sum=0

while n>0:
    d=math.floor(n%10)
    sum+=d
    n=n/10
print("sum of digit",sum)