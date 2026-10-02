l=[1,3,4,2,5,1,5,2,3]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(l[j])
