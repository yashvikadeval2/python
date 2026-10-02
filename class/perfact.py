

# class first:
#     def __init__(self):
#         self.n=int(input("enter n:"))
    
#     def logic(self):
#         self.p=[]
#         num=1
#         while num<=self.n:
#             t=num
#             sum=0
#             i=1

#             while i<t:
#                 if t%i==0:
#                     sum+=i
#                 i+=1
#             if sum==num:
#                 self.p+=[num]
#             num+=1
#     def disp(self):
#         print(self.p)

# f=first()
# f.logic()
# f.disp()

class first:
    def __init__(self):
        self.n=int(input("Enter n :"))

    def logic(self):
        self.num=1
        self.r=[]
        while self.num<=self.n:
            t=self.num
            sum=0
            i=1

            while i<t:
                if t%i==0:
                    sum+=i
                i+=1
            
            if sum==self.num:
                self.r="This number is perfect number"
            else:
                self.r="This number is not perfect number"
            self.num+=1

    def disp(self):
        print(self.r)
    
f=first()
f.logic()
f.disp()
