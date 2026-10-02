import math
a=0
r=0
t=0

while a<=10:
    n=a

    while n!=0:
        t=math.floor(n%10)
        r=r+t
        n=math.floor(n/10)
    if a==r:
        print(r)
    r=0
    t=0
    a+=1

while a<=100:
    n=a

    while n!=0:
        t=math.floor(n%10)
        r=r+(t*t)
        n=math.floor(n/10)
    if a==r:
        print(r)
    r=0
    t=0
    a+=1    
    
a=100
while a<=1000:
    n=a

    while n!=0:
        t=math.floor(n%10)
        r=r+(t*t*t)
        n=math.floor(n/10)
    if a==r:
        print(r)
    r=0
    t=0
    a+=1

a=1000    
while a<=10000:
    n=a

    while n!=0:
        t=math.floor(n%10)
        r=r+(t*t*t*t)
        n=math.floor(n/10)
    if a==r:
        print(r)
    r=0
    t=0
    a+=1

   
    
