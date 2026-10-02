t=(1,2,3,4,5,6,7)
cnt=0
sum=0
for i in range(len(t)):
    print("t[%d]=%d"%(cnt,t[i]))
    cnt+=1
    if i%2!=0:
        sum+=t[i]

print("sum = ",sum)
