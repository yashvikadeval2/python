t=(1,2,4,1,4,2,5,6,7,1,2,6,4,6)
print(t)
c=0

for i in t:
    x=0
    for j in t:
        if i==j:   
            x+=1  
        if x>c:  
            c=x
            f=i

print("most frequence element:",f)
