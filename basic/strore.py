p1=[1,2,2,3,4,5,5,3]
p2=[]
n=len(p1)

for i in range(n):
    for j in range(i+1,n):
        if p1[i]==p1[j]:
            t=0
            for k in range(len(p2)):
                if p1[j]==p2[k]:
                    t=1

            if t==0:
                p2+=[p1[j]]

for i in range(n):
    t=0
    for j in range(i):
        if p1[i]==p1[j]:
            t=1

    if t==1:
        print(p1[i])

