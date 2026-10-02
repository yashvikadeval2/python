l=[10,20,30,40,50]

new=25
pos=2
l=l+[0]

for i in range(len(l)-1,pos-1,-1):
    l[i] = l[i-1]
l[pos-1] = new

print(l)


