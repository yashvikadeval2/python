import math
n=int(input("enter n:"))
x=n
t=0

while n>0:
    a=math.floor(n%10)
    t=t*10+a
    n=math.floor(n/10)

if x==t:
    print("this number is palindron number")
else:
    print("this number is not palindron number")
