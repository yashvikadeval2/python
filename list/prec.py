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


#palidrom print
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




    


