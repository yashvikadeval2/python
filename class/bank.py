print("1 IS SAVEING ACCOUNT")
print("2 IS CURRENT ACCOUNT")
n=int(input("enter choice :"))
if n==1:
    a=20000
    print(a)
if n==2:
    a=30000
    print(a)

password="yashvi123"

cnt=0
while cnt<3:
    p=input("enter password :")

    if p==password:
        c=input("enter confirm password:")
        print("your account open successfully")
        break
    else:
        cnt+=1

        if cnt<3:
            print("wrong password! enter password again!")
        else:
            print("exit")

print("1. widraw")
print("2. deposite")
print("3. check balance")
print("4.change password")
print("5. print passbook")
print("6.exit")

n1=input("enter choice:")
aa=a
if n1=="1":
    cnt=0
    while cnt<3:
        p=input("enter password :")

        if p==password:
            wid=int(input("enter widraw amount :"))
            totala=a-5000
            if totala>=wid:
                print("your account is widraw")
                totalam=aa-wid
                print(totalam)
            break
        else:
            cnt+=1

            if cnt<3:
                print("wrong password! enter password again!")
            else:
                print("exit")

if n1=="2":
    cnt=0
    while cnt<3:
        p=input("enter password :")

        if p==password:
            dep=int(input("enter deposite amount :"))
            a+=dep
            print(a)
            break
        else:
            cnt+=1

            if cnt<3:
               print("wrong password! enter password again!")
            else:
                 print("exit")

