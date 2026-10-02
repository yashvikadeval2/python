from datetime import datetime
import os

# Create files if they don't exist
if not os.path.exists("account.txt"):
    f = open("account.txt", "w")
    f.write("20000\n")
    f.write("abc123")
    f.close()

if not os.path.exists("passbook.txt"):
    open("passbook.txt", "w").close()


# -------------------- Read Account --------------------

def read_account():
    f = open("account.txt", "r")
    data = f.readlines()
    f.close()

    balance = int(data[0].strip())
    password = data[1].strip()

    return balance, password


# -------------------- Save Account --------------------

def save_account(balance, password):
    f = open("account.txt", "w")
    f.write(str(balance) + "\n")
    f.write(password)
    f.close()


# -------------------- Add Transaction --------------------

def add_transaction(msg):
    f = open("passbook.txt", "a")
    f.write("\n")
    f.close()


# -------------------- Account Type --------------------

while True:

    print("1 IS SAVING ACCOUNT")
    print("2 IS CURRENT ACCOUNT")

    ch = int(input("Enter choice : "))

    if ch == 1:
        balance = 20000
        break

    elif ch == 2:
        balance = 30000
        break

    else:
        print("Invalid Choice")


# -------------------- Password Create --------------------

while True:

    password = input("Create Password : ")

    alpha = 0
    digit = 0
    valid = True

    for i in password:

        a = ord(i)

        if 65 <= a <= 90 or 97 <= a <= 122:
            alpha += 1

        elif 48 <= a <= 57:
            digit += 1

        else:
            valid = False
            break

    if alpha > 0 and digit > 0 and valid:
        break

    else:
        print("Invalid Password")

save_account(balance, password)

print("Account Created Successfully")


# ================= MENU =================

while True:

    balance, password = read_account()

    print("\n1 Withdraw")
    print("2 Deposit")
    print("3 Check Balance")
    print("4 Change Password")
    print("5 Passbook")
    print("6 Exit")

    choice = input("Enter Choice : ")

    # Withdraw
    if choice == "1":

        p = input("Enter Password : ")

        if p == password:

            amt = int(input("Withdraw Amount : "))

            if balance - amt >= 5000:

                balance -= amt

                save_account(balance, password)

                dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                add_transaction(
                    f"Withdraw ₹{amt} Balance ₹{balance} {dt}"
                )

                print("Withdraw Successful")

            else:
                print("Minimum Balance ₹5000 Required")

        else:
            print("Wrong Password")

    # Deposit
    elif choice == "2":

        p = input("Enter Password : ")

        if p == password:

            amt = int(input("Deposit Amount : "))

            if amt <= 25000:

                balance += amt

                save_account(balance, password)

                dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                add_transaction(
                    f"Deposit ₹{amt} Balance ₹{balance} {dt}"
                )

                print("Deposit Successful")

            else:
                print("Maximum Deposit Limit ₹25000")

        else:
            print("Wrong Password")

    # Balance
    elif choice == "3":

        p = input("Enter Password : ")

        if p == password:

            print("Current Balance =", balance)

        else:
            print("Wrong Password")

    # Change Password
    elif choice == "4":

        old = input("Old Password : ")

        if old == password:

            while True:

                new = input("New Password : ")

                alpha = 0
                digit = 0
                valid = True

                for i in new:

                    a = ord(i)

                    if 65 <= a <= 90 or 97 <= a <= 122:
                        alpha += 1

                    elif 48 <= a <= 57:
                        digit += 1

                    else:
                        valid = False
                        break

                if alpha > 0 and digit > 0 and valid:
                    break

                else:
                    print("Invalid Password")

            save_account(balance, new)

            print("Password Changed Successfully")

        else:
            print("Wrong Password")

    # Passbook
    elif choice == "5":

        p = input("Enter Password : ")

        if p == password:

            f = open("passbook.txt", "r")

            data = f.read()

            f.close()

            if data == "":
                print("No Transactions")

            else:
                print(data)

            print("Current Balance =", balance)

        else:
            print("Wrong Password")

    # Exit
    elif choice == "6":

        print("Thank You")
        break

    else:
        print("Invalid Choice")