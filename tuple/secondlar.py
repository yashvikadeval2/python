t=(45,75,12,46,76,89,23)
l=list(t)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t

print(l)
t=tuple(l)
n=len(l)

for i in range(n-1):
    if i==n-2:
        print("second largest",t[i])
