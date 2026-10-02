#strong number
'''import math
n=int(input("enter n:"))
sum=0
t=n
while n>0:
    r=math.floor(n%10)
    fact=1
    i=1
    while i<=r:
        fact=fact*i
        i+=1
    sum+=fact
    n=math.floor(n/10)

if sum==t:
    print("strong")
else:
    print("not")'''

#strong print
'''import math
n=int(input("enter n:"))
num=1
while num<=n:
    sum=0
    t=num
    while t>0:
        r=math.floor(t%10)
        fact=1
        i=1
        while i<=r:
            fact=fact*i
            i+=1
        sum+=fact
        t=math.floor(t/10)



    if sum==num:
        print(num)
    num+=1'''

#armstrong
'''import math
n=int(input("enter n:"))
sum=0
t=n
while n>0:
    r=math.floor(n%10)
    sum=sum+(r*r*r)
    n=n/10

if sum==t:
    print("armstrong")
else:
    print("not")'''

#armstrong print
'''import math
n=int(input("enter n:"))

for i in range(n+1):
    sum=0
    t=i
    while t>0:
        r=math.floor(t%10)
        sum=sum+(r*r*r)
        t=t/10

    if sum==i:
        print(i)'''
#print palidrom
'''import math
n=int(input("enter n:"))

for i in range(n):
    sum=0
    t=i
    while t>0:
        r=math.floor(t%10)
        sum=sum*10+r
        t=math.floor(t/10)

    if sum==i:
        print(i)'''

#pali
'''import math
n=int(input("enter n:"))
t=n
sum=0
while n>0:
    r=math.floor(n%10)
    sum=sum*10+r
    n=math.floor(n/10)

if sum==t:
    print("palid")
else:
    print("not")'''

#perfact
'''n=int(input("enter n:"))
t=n
sum=0
i=1
while i<n:
    if n%i==0:
        sum=sum+i
    i+=1

if sum==t:
    print("perfact")
else:
    print("not")'''

#print perfact
'''n=int(input("enter n:"))
num=1
while num<=n:
    t=num
    sum=0
    i=1
    
    while i<t:
        if t%i==0:
            sum+=i
        i+=1

    if sum==num:
        print(num)
    num+=1'''

#insert
'''l=[10,20,30,40,50]
new=25
pos=2
l=l+[0]
for i in range(len(l)-1,pos-1,-1):
    l[i]=l[i-1]
        
l[pos-1]=new

print(l)'''

'''l=[34,78,56,43,90,23,85]
pos=int(input("Enter position of value : "))
n=int(input("Enter new value : "))

x=[0,0,0,0,0,0,0,0]
j=0
for i in range(len(x)):
    if i==pos:
        x[i]=n
    else:
        x[i]=l[j]
        j=j+1
        
for i in x:
    print(i)'''

#delete
'''l=[10,20,30,40,50,60]
v=20
for i in range(len(l)):
    if l[i]==v:
        for j in range(i,len(l)-1):
            l[j]=l[j+1]

for i in range(len(l)-1):
    print(l[i])'''

#merge
'''l=[1,2,3]
l1=[4,5,6]
l11=l+l1
print(l11)'''

#second largest
'''l=[23,56,12,45,34,78,22]

l.sort()
print(l)

for i in range(len(l)-1):
    if i==len(l)-2:
        print(l[i])'''

#remove duplicate
'''l=[1,3,4,6,2,4,6,5,5,7,4]
n=len(l)
for i in range(n):
    for j in range(i+1,n-1):
        if l[i]==l[j]:
            for s in range(j,n-1):
                l[s]=l[s+1]
            n-=1

for i in range(n-1):
    print(l[i])'''

#unique
'''l=[1,2,1,3,4,4,5,6,3]
print(l)
n=int(input("enter n:"))

cnt=0

for i in l:
    if i==n:
        cnt+=1

if cnt==1:
    print("unique")
else:
    print("not")'''


#sum of even
'''t=(1,3,2,4,5,6,7)
l=list(t)
sum=0
for i in l:
    if i%2==0:
        sum+=i
t=tuple(l)
print("sum = ",sum)'''





    
        


        
    
    
    
        

    

        
    
    
     



