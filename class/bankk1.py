from datetime import datetime
while True:
    print("1 IS SAVING ACCOUNT")
    print("2 IS CURRENT ACCOUNT")

    n = int(input("Enter your choice : "))

    if n==1 or n==2:
        if n == 1:
            a = 20000
            print(a)
            break
        else:
            a = 30000
            print(a)
            break
    else:
        print("Enter valide choice :")
    
while True:

    password = input("Enter password :")
    al=0
    di=0
    valid=True

    for i in password:
        aa=ord(i)
        if (65<=aa<=90) or (97<=aa<=122):
            al+=1
        elif (48<=aa<=57):
            di+=1
        else:
            valid=False
            break

    if al>0 and di>0 and valid:
        print("sucess....")
        break
    else:
        print("wrong password..!")
        
cnt = 1
while cnt <= 3:
    p = input("Enter confirm password : ")

    if password == p:
        print("YOUR ACCOUNT IS OPEN SUCCESSFULLY..!")
        break
    else:
        cnt += 1
        if cnt <= 3:
            print("WRONG PASSWORD...")
        else:
            print("EXIT")
            exit()

transactions = []
while True:

    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Change Password")
    print("5. Print Passbook")
    print("6. Exit")

    n1 = input("Enter your choice : ")

    # Withdraw
    if n1 == "1":
       
        cnt = 1
        while cnt <= 3:
            
            p = input("Enter password : ")
            if password == p:
                print("")

                break
            else:
                cnt += 1
                if cnt <= 3:
                    print("WRONG PASSWORD...")
                else:
                    print("")
                    # exit()


        if p == password:
            wid = int(input("Enter withdraw amount : "))

            if a - wid >= 5000:
                a -= wid

                dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                transactions.append(
                    f"Withdraw  ₹{wid}  Balance: ₹{a}  {dt}"
                )


                print("WITHDRAW SUCCESSFUL")
                print("Balance =", a)
            else:
                print("Minimum balance ₹5000 required.")
        else:
            print("Wrong Password")

    # Deposit
    elif n1 == "2":
        
        cnt = 1
        while cnt <= 3:
            p = input("Enter password : ")

            if password == p:
                print("")
                break
            else:
                cnt += 1
                if cnt <= 3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()
        if p == password:
            dep = int(input("Enter deposit amount : "))

            if dep <= 25000:
                a += dep
                dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                transactions.append(
                    f"Deposit  ₹{dep}  Balance: ₹{a}  {dt}"
                )
                print("DEPOSIT SUCCESSFUL")
                print("Balance =", a)
            else:
                print("Maximum deposit limit is ₹25000")
        else:
            print("Wrong Password")

     # Check Balance
    elif n1 == "3":

        cnt = 1
        while cnt <= 3:
            p = input("Enter password : ")

            if password == p:
                print("")

                break
            else:
                cnt += 1
                if cnt <= 3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()

        print("Current Balance =", a)

    # Change Password
    elif n1 == "4":
        
        cnt = 1
        while cnt <= 3:
            p = input("Enter old password : ")

            if password == p:
                print("")

                break
            else:
                cnt += 1
                if cnt <= 3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()

        if p == password:
            # passw = input("Enter new password : ")
            while True:
                password = input("Enter new password : ")
                al=0
                di=0
                valid=True

                for i in password:
                    aa=ord(i)
                    if (65<=aa<=90) or (97<=aa<=122):
                        al+=1
                    elif (48<=aa<=57):
                        di+=1
                    else:
                        valid=False
                        break

                if al>0 and di>0 and valid:
                    print("sucess")
                    break
                else:
                    print("wrong...")
            
            cnt = 1
            while cnt <= 3:
                pp=input("Confirm new password : ")
                if password == pp:
                    print("")

                    break
                else:
                    cnt += 1
                    if cnt <= 3:
                        print("WRONG PASSWORD...")
                    else:
                        print("EXIT")
                        # exit()
       
    # Passbook
    elif n1 == "5":
        
        cnt = 1
        while cnt <= 3:
            p = input("Enter password : ")

            if password == p:
                print("")

                break
            else:
                cnt += 1
                if cnt <= 3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()

        if len(transactions) == 0:
            print("No Transactions Found")
        else:
            for t in transactions:
                print(t)
        print("Current Balance :", a)

    # Exit
    elif n1 == "6":
        print("Thank You For Visit!")
        break

    else:
        print("Invalid Choice")