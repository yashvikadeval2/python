ro=int(input("enter roll number = "))
name=input("enter name = ")
s1=int(input("value of s1 = "))
s2=int(input("value of s2 = "))
s3=int(input("value of s3 = "))
s4=int(input("value of s4 = "))
s5=int(input("value of s5 = "))

print("Rno = ",ro)
print("Name = ",name)
print("s1 = ",s1)
print("s2 = ",s2)
print("s3 = ",s3)
print("s4 = ",s4)
print("s5 = ",s5)

total=s1+s2+s3+s4+s5
per=total/5

print("total = ",total)
print("per = ",per)

if s1>s2 and s1>s3 and s1>s4 and s1>s5:
    print("s1 is max",s1)
elif s2>s3 and s2>s4 and s2>s5:
    print("s2 is max",s2)
elif s3>s4 and s3>s5:
    print("s3 is max",s3)
elif s4>s5:
    print("s4 is max",s4)
else:
    print("s5 is max",s5)

if s1<s2 and s1<s3 and s1<s4 and s1<s5:
    print("s1 is min",s1)
elif s2<s3 and s2<s4 and s2<s5:
    print("s2 is min",s2)
elif s3<s4 and s3<s5:
    print("s3 is min",s3)
elif s4<s5:
    print("s4 is min",s4)
else:
    print("s5 is min",s5)

if per>90:
    print("A grade")
elif per>80:
    print("B grade")
elif per>70:
    print("c grade")
elif per>50:
    print("d grade")
elif per>35:
    print("e grade")
else:
    print("fail")

cnt=0;

if s1<35:
    cnt+=1;
elif s2<35:
    cnt+=1;
elif s3<35:
    cnt+=1;
elif s4<35:
    cnt+=1;
elif s5<35:
    cnt+=1;
else:
    cnt=0;

if cnt==0:
    print("PASS")
elif cnt>=1:
    print("ATKT")
else:
    print("FAIL")


    



    

