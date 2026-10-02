'''l=[1,2,3,4,5]
l1=[]

for i in l:
    l1.append(i*i)

s=set(l1)
print(s)'''


l=[1,2,3,4,5]
s=set()

for i in l:
    s.add(i*i)
print(s)
