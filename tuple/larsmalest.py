t=(1,2,3,4,5)

max=t[0]
for i in t:
    if max<=i:
        max=i

print("max = ",max)


min=t[0]
for i in t:
    if min>=i:
        min=i

print("min = ",min)
