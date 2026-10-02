l=[1,4,3,1,4,6,3,5,2]

n=len(l)
 
for i in range(n):
    for j in range(i+1,n-1):
        if l[i]==l[j]:
            for k in range(j,n-1):
                l[k]=l[k+1]
            n-=1
       
            
for i in range(n-1):    
    print(l[i])
