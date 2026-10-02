# class first:
#     def __init__(self):
#         self.n=int(input("enter n:"))

#     def logic(self):
#         self.r=[]
#         for i in range(1,self.n):
#             cnt=0
#             for j in range(1,i+1):
#                 if i%j==0:
#                     cnt+=1
#             if cnt<=2:
#                 self.r+=[i]
#     def disp(self):
#         print(self.r)
# f=first()
# f.logic()
# f.disp()

class first:
    def __init__(self):
        self.n=int(input("Enter n :"))

    def logic(self):
        self.r=[]
        for i in range(1,self.n):
            self.cnt=0
            for j in range(1,i+1):
                if i%j==0:
                    self.cnt+=1
            if self.cnt<=2:
                self.r="This number is prime number"
            else:
                self.r="This number is not prime number"
                    
    
    def disp(self):
        print(self.r)

f=first()
f.logic()
f.disp()