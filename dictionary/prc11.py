d=[10,20,30,20,10,40]

n=len(d)

for i in range(n):
    for j in range(i+1,n):
        if d[i]==d[j]:
            print(d[j])
            

            