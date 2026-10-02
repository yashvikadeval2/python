from datetime import datetime

class BankAccount:

    def __init__(self):
        print("1 IS SAVING ACCOUNT")
        print("2 IS CURRENT ACCOUNT")

        n=int(input("Enter your choice : "))

        if n==1:
            self.balance = 20000
        elif n==2:
            self.balance = 30000
        else:
            print("Invalid Choice")
            exit()

        print("Opening Balance =", self.balance)

        self.password ="yashvi123"
        self.transactions=[] 
    def login(self):
        cnt=1
        while cnt<=3:
            p=input("Enter password : ")

            if p==self.password:
                print("YOUR ACCOUNT IS OPEN SUCCESSFULLY..!")
                return
            else:
                cnt+=1
                if cnt<=3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()

    def withdraw(self):
        p=input("Enter password : ")

        if p==self.password:
            wid=int(input("Enter withdraw amount : "))

            if self.balance-wid>=5000:
                self.balance-=wid

                dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.transactions.append(
                    f"Withdraw ₹{wid} Balance: ₹{self.balance} {dt}"
                )

                print("WITHDRAW SUCCESSFUL")
                print("Balance =", self.balance)
            else:
                print("Minimum balance ₹5000 required.")
        else:
            print("Wrong Password")

    def deposit(self):
        p = input("Enter password : ")

        if p == self.password:
            dep = int(input("Enter deposit amount : "))

            if dep <= 25000:
                self.balance += dep

                dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.transactions.append(
                    f"Deposit ₹{dep} Balance: ₹{self.balance} {dt}"
                )

                print("DEPOSIT SUCCESSFUL")
                print("Balance =", self.balance)
            else:
                print("Maximum deposit limit is ₹25000")
        else:
            print("Wrong Password")

    def check_balance(self):
        print("Current Balance =", self.balance)

    def change_password(self):
        p = input("Enter old password : ")

        if p == self.password:
            new_pass = input("Enter new password : ")
            confirm_pass = input("Confirm new password : ")

            if new_pass == confirm_pass:
                self.password = new_pass
                print("Password changed successfully")
            else:
                print("Password does not match")
        else:
            print("Wrong Password")

    def passbook(self):
        if len(self.transactions) == 0:
            print("No Transactions Found")
        else:
            print("\n----- PASSBOOK -----")
            for t in self.transactions:
                print(t)

        print("Current Balance :", self.balance)

    def disp(self):
        while True:
            print("\n1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Change Password")
            print("5. Print Passbook")
            print("6. Exit")

            choice = input("Enter your choice : ")

            if choice == "1":
                self.withdraw()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.check_balance()

            elif choice == "4":
                self.change_password()

            elif choice == "5":
                self.passbook()

            elif choice == "6":
                print("Thank You!")
                break

            else:
                print("Invalid Choice")


# Object Creation
obj = BankAccount()
obj.login()
obj.disp()