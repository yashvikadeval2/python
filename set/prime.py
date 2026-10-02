s=set()

for i in range(1,20):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1

    if cnt<=2:
        s.add(i)

print(s)
