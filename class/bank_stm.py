from datetime import datetime

class Bank:

    def __init__(self):
        self.balance = 0
        self.password = ""
        self.transactions = []

    # Account Type Selection
    def create(self):
        while True:
            print("1. Saving Account")
            print("2. Current Account")

            c = int(input("Enter your choice: "))

            if c == 1:
                self.balance = 20000
                print("Saving Account Created")
                print("Balance =", self.balance)
                break

            elif c == 2:
                self.balance = 30000
                print("Current Account Created")
                print("Balance =", self.balance)
                break

            else:
                print("Invalid Choice")

        self.set_password()
        self.confirm_password()
        print("YOUR ACCOUNT IS OPEN SUCCESSFULLY..!")

    # Password Validation
    def validate_password(self, password):
        alpha = 0
        digit = 0

        for ch in password:
            if ch.isalpha():
                alpha += 1
            elif ch.isdigit():
                digit += 1
            else:
                return False

        return alpha > 0 and digit > 0

    # Set Password
    def set_password(self):
        while True:
            pwd = input("Enter Password: ")

            if self.validate_password(pwd):
                self.password = pwd
                print("Password Created Successfully")
                break
            else:
                print("Password must contain letters and digits only")

    # Confirm Password
    def confirm_password(self):
        count = 1

        while count <= 3:
            cpwd = input("Confirm Password: ")

            if cpwd == self.password:
                return

            count += 1

            if count <= 3:
                print("Wrong Password")
            else:
                print("Exit")
                exit()

    # Password Check
    def verify_password(self):
        count = 1

        while count <= 3:
            pwd = input("Enter Password: ")

            if pwd == self.password:
                return True

            count += 1

            if count <= 3:
                print("Wrong Password")
            else:
                print("Exit")
                return False

    # Withdraw
    def withdraw(self):
        if not self.verify_password():
            return

        amount = int(input("Enter Withdraw Amount: "))

        if self.balance - amount >= 5000:
            self.balance -= amount

            dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            self.transactions.append(
                f"Withdraw ₹{amount}  Balance ₹{self.balance}  {dt}"
            )

            print("Withdraw Successful")
            print("Balance =", self.balance)

        else:
            print("Minimum balance ₹5000 required")

    # Deposit
    def deposit(self):
        if not self.verify_password():
            return

        amount = int(input("Enter Deposit Amount: "))

        if amount <= 25000:
            self.balance += amount

            dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            self.transactions.append(
                f"Deposit ₹{amount}  Balance ₹{self.balance}  {dt}"
            )

            print("Deposit Successful")
            print("Balance =", self.balance)

        else:
            print("Maximum Deposit Limit is ₹25000")

    # Check Balance
    def check_balance(self):
        if self.verify_password():
            print("Current Balance =", self.balance)

    # Change Password
    def change_password(self):
        print("Verify Old Password")

        if not self.verify_password():
            return

        while True:
            new_pwd = input("Enter New Password: ")

            if self.validate_password(new_pwd):
                break
            else:
                print("Invalid Password")

        count = 1

        while count <= 3:
            cpwd = input("Confirm New Password: ")

            if cpwd == new_pwd:
                self.password = new_pwd
                print("Password Changed Successfully")
                return

            count += 1

            if count <= 3:
                print("Wrong Password")
            else:
                print("Exit")
                return

    # Passbook
    def print_passbook(self):
        if not self.verify_password():
            return
        if len(self.transactions) == 0:
            print("No Transactions Found")
        else:
            for t in self.transactions:
                print(t)

        print("Current Balance =", self.balance)

    # Menu
    def menu(self):
        while True:
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Change Password")
            print("5. Print Passbook")
            print("6. Exit")

            ch = input("Enter Your Choice: ")

            if ch == "1":
                self.withdraw()

            elif ch == "2":
                self.deposit()

            elif ch == "3":
                self.check_balance()

            elif ch == "4":
                self.change_password()

            elif ch == "5":
                self.print_passbook()

            elif ch == "6":
                print("Thank You For Visit!")
                break

            else:
                print("Invalid Choice")


# Main Program
obj = Bank()
obj.create()
obj.menu()