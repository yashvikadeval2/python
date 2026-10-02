import math
class first:
    def __init__(self):
        self.n=int(input("Enter n :"))
    
    def logic(self):
        num=10
        self.g=[]
        while num<=self.n:
            t=num
            r=0

            while t!=0:
                a=math.floor(t%10)
                r=r*10+a
                t=math.floor(t/10)

            if r==num:
                self.g="This number is palindrome number"
            else:
                self.g="This number is not palindrome number"
            num+=1

    def disp(self):
        print(self.g)

f=first()
f.logic()
f.disp()










