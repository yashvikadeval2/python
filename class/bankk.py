from datetime import datetime

while True:
    print("1 IS SAVING ACCOUNT")
    print("2 IS CURRENT ACCOUNT")

    n = int(input("Enter your choice : "))

    if n== 1:
        a=20000
        print(a)
        break
    elif n== 2:
        a=30000
        print(a)
        break    
    else:
        print("Invalid Choice")
        #exit()



transactions = []

while True:
    password = input("Create password: ")

    alpha = 0
    digit = 0
    valid = True

    for ch in password:
        a = ord(ch)

        if (65 <= a <= 90) or (97 <= a <= 122):
            alpha += 1
        elif 48 <= a <= 57:
            digit += 1
        else:
            valid = False
            break

    if alpha > 0 and digit > 0 and valid:
        print("Success")
        break
    else:
        print("Password must contain only letters and digits")
        

cnt=1
while cnt<= 3:
    p=input("Enter password : ")

    if password==p:
        print("YOUR ACCOUNT IS OPEN SUCCESSFULLY..!")
        break
    else:
        cnt+=1
        if cnt<=3:  
            print("WRONG PASSWORD...")
        else:
            print("EXIT")
            #exit()
while True:

    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Change Password")
    print("5. Print Passbook")
    print("6. Exit")

    n1=input("Enter your choice : ")

    # Withdraw
    if n1=="1":
        p=input("Enter password : ")

        if p==password:
            wid=int(input("Enter withdraw amount : "))

            if a-wid>=5000:
                a-=wid

                dt=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                transactions.append(
                    f"Withdraw ₹{wid}Balance:₹{a}{dt}"
                )


                print("WITHDRAW SUCCESSFUL")
                print("Balance =",a)
            else:
                print("Minimum balance ₹5000 required.")
        else:
           print("Wrong Password")
           
       
            

    # Deposit
    elif n1=="2":
        p=input("Enter password : ")

        if p==password:
            dep=int(input("Enter deposit amount : "))

            if dep<=25000:
                a+=dep
                dt=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                transactions.append(
                    f"Deposit  ₹{dep}Balance:₹{a}{dt}"
                )
                print("DEPOSIT SUCCESSFUL")
                print("Balance =",a)
            else:
                print("Maximum deposit limit is ₹25000")
        else:
            print("Wrong Password")
     # Check Balance
    elif n1=="3":
        print("Current Balance =",a)

    # Change Password
    elif n1=="4":
        p = input("Enter old password : ")

        if p==password:
            password = input("Enter new password : ")
            pp=input("Confirm new password : ")
            if password == pp:
                print("Password changed successfully")
            else:
                print("Password does not match")
        else:
            print("Wrong Password")

    # Passbook
    elif n1=="5":
        if len(transactions)==0:
            print("No Transactions Found")
        else:
            for t in transactions:
                print(t)
        print("Current Balance :",a)

    # Exit
    elif n1=="6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")