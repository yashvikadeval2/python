t=(1,4,3,1,4,6,3,5,2)
l=list(t)
n=len(t)
 
for i in range(n):
    for j in range(i+1,n-1):
        if l[i]==l[j]:
            for k in range(j,n-1):
                l[k]=l[k+1]
            n-=1
t=tuple(l)      
            
for i in range(n-1):    
    print(t[i])
