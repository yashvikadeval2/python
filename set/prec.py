#prime print
'''n=int(input("enter n:"))

for i in range(n):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        print(i)'''


#armstrong print
'''import math
n = int(input("Enter n: "))

for i in range(n + 1):
    t = i
    sum = 0

    while t > 0:
        a = math.floor(t % 10)
        sum= sum + (a*a*a)
        t = t / 10

    if sum == i:
        print(i)'''


'''#palidrom print
import math
n = int(input("Enter n: "))

for i in range(n + 1):
    t = i
    sum = 0

    while t > 0:
        a = math.floor(t % 10)
        sum= sum * 10 + a
        t = t / 10

    if sum == i:
        print(i)

for i in range(1,5):
    for s in range(i,5):
        print(" ",end="")
    for j in range(1,i*2):
        if j==1 or j==i*2-1:
            print("x",end="")
        else:
            print(" ",end="")
    print()

for i in range(1,6):
    print("x ",end="")'''

a=int(input("enter a = "))
b=int(input("enter b = "))
c=int(input("enter c = "))
d=int(input("enter d = "))
e=int(input("enter e = "))

print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)
print("e = ",e)

if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("a is max")
            else:
                print("e is max")
        else:
            if d>e:
                print("d is max")
            else:
                print("e is max")
else:
    if b>c:
        if b>d:
            if b>e:
                print("b is max")
            else:
                print("e is max")
        else:
            if d>e:
                print("d is max")
            else:
                print("e is max")
        




    


