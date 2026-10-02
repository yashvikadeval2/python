'''l=[34,56,71,12,97,57]
l1=[]

for i in l:
    if i%2==0:
        l1.append(i)

s=set(l1)
print(s)'''

l=[12,56,34,78,45,98,45]
s=set()

for i in l:
    if i%2==0:
        s.add(i)

print(s)
