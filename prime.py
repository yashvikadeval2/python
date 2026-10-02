n=int(input("enter n:"))

i=1
cnt=0

while i<=n:
    if n%i==0:
        print(i)
        cnt+=1
    i+=1

if cnt<=2:
    print("this number is prime number")
else:
    print("this number is not prime number")
