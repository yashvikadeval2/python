import math
class first:
    def __init__(self):
        self.n=int(input("enter n : "))
    
    def logic(self):
        num=10
        self.get=[]
        while num<=self.n:
            t=num
            r=0

            while t!=0:
                a=math.floor(t%10)
                r=r*10+a
                t=math.floor(t/10)

            if r==num:
                self.get+=[num]
            num+=1

    def disp(self):
        for i in self.get:
            print(i)

f=first()
f.logic()
f.disp()











