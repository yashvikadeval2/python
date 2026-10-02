f=open("bank.txt","a")

while True:
    print("1.create account")
    print("2.deposit")
    print("3.withdraw")
    print("4.transfer funds")
    print("5.check balance")
    print("6.exit")

    n=int(input("Enter n : "))

    if n==1:
        password=input("Enter password : ")
        account_number=input("Enter account number : ")
        name=input("Enter name : ")
        balance=float(input("Enter balance : "))
        if f.tell()==0:
            f.write(f"Ac_Number\tName\t\tBalance\t\tPassword")
        f.write(f"\n{account_number}\t\t{name}\t\t{balance}\t\t{password}")

    elif n==6:
        print("Thank you for using the banking system!")
        exit()