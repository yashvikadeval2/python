'''t=(1,2,3,4,5,6)
l=list(t)
l.insert(2,"hello")

t=tuple(l)
print(t)
print(type(t))'''


t = (10, 20, 30, 40, 50, 60)
print(t)
count = 0
for i in t:
 print("t[%d] = %d"%(count, i))
 count = count+1
