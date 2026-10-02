import math
class first:
    def __init__(self):
        self.n=int(input("enter n:"))
    
    def logic(self):
        self.p=[]
        for i in range(1,self.n):
            sum=0
            t=i
            while t>0:
                r=math.floor(t%10)
                sum=sum+(r*r*r)
                t=t/10
            if sum==i:
                self.p+=[i]
    
    def disp(self):
        print(self.p)

f=first()
f.logic()
f.disp()