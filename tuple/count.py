t=(6,4,7,8,9,1,2,3,5,3,4,3)

'''cnt=0

for i in t:
    if i==3:
        cnt+=1
print(cnt)'''

l=list(t)
t=tuple(l)
l=l.count(3)
print(l)
print(t)
