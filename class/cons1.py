class first:
    def __init__(self):
        self.n=int(input("enter n:"))
    
    def logic(self):
        a=0
        b=1
        self.r=[]
        while a<=self.n:
            self.r+=[a]
            c=a+b
            a=b
            b=c
        
    def disp(self):
        print(self.r)


f=first()
f.logic()
f.disp()
        