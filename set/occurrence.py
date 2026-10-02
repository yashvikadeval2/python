l=[3,5,4,1,7,3,2,15,4,3,2,1,6,5,4,15]
s=set(l)
print(l)

for i in s:
    cnt=0
    for j in l:
        if i==j:
            cnt+=1
    print(i," = ",cnt,"time")
