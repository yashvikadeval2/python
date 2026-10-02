class first:
    def __init__(self):
        self.n=int(input("enter n:"))
    
    def logic(self):
        self.fact=1
        self.r=[]
        for i in range(1,self.n+1):
            self.fact=self.fact*i
            self.r+=[self.fact]
    def disp(self):
        print(self.r)

f=first()
f.logic()
f.disp()