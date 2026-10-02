s1={1,2,3,4,5}
s2={6,7}

'''print(s1|s2)

print(s1.union(s2))

print(s1&s2)

print(s1.intersection(s2))

s1.intersection_update(s2)
print(s1)

print(s1-s2)

print(s1.difference(s2))

#s1=s1.symmetric_difference(s2)
#print(s1)

s1=s1.symmetric_difference_update(s2)
print(s1)

x=s1.copy()
print(x)

x = s1.intersection(s2)
print(x)'''

x = s1.isdisjoint(s2)
print(x)


                    
