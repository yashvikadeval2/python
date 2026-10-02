# import math
# class first:
#     def __init__(self):
#         self.n=int(input("enter n:"))
    
#     def logic(self):
#         self.p=[]
#         num=1
#         while num<=self.n:
#             sum=0
#             t=num
#             while t>0:
#                 r=math.floor(t%10)
#                 fact=1
#                 i=1
#                 while i<=r:
#                     fact=fact*i
#                     i+=1
#                 sum+=fact
#                 t=math.floor(t/10)
#             if sum==num:
#                 self.p+=[num]
#             num+=1
#     def disp(self):
#         print(self.p)
# f=first()
# f.logic()
# f.disp()

import math
class first:
    def __init__(self):
        self.n=int(input("Enter n :"))

    def logic(self):
        self.num=1
        self.r=[]
        while self.num<=self.n:
            sum=0
            t=self.num
            
            while t>0:
                r=math.floor(t%10)
                fact=1
                i=1

                while i<=r:
                    fact=fact*i
                    i+=1
                sum+=fact
                t=math.floor(t/10)
            if sum==self.num:
                self.r="This number is strong number"
            else:
                self.r="This number is not strong number"
            self.num+=1
    
    def disp(self):
        print(self.r)


f=first()
f.logic()
f.disp()