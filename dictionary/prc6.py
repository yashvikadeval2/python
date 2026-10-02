l=["apple","banana","apple","orange","banana","grape","apple","grape"]
s=set(l)
print(l)

for i in s:
    cnt=0
    for j in l:
        if i==j:
            cnt+=1
    print(i," = ",cnt,"time")