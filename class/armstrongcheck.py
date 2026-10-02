import math
class first:
    def __init__(self):
        self.n=int(input("Enter n :"))
        self.num=self.n

    def logic(self):
        self.r=0
        b=0
        self.aa=0
        while self.n>0:
            t=math.floor(self.n%10)
            b+=1
            self.n=math.floor(self.n/10)
        
        self.a=self.nn

        while self.num>0:
            d=math.floor(self.num%10)
            self.r=self.r+math.pow(d,b)
            self.num=math.floor(self.num/10)

        if self.r==self.a:
            self.aa="This number is armstrong number"
        else:
            self.aa="This number is not armstrong number"

    def disp(self):
        print(self.aa)

f=first()
f.logic()
f.disp()

