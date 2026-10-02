t=(1,2,3,1,2,4,5,2,3,7,6)

n=int(input("enter n:"))

c=0

for i in t:
    if i==n:
        c+=1

if c==1:
    print("unique number")
else:
    print("not unique")
