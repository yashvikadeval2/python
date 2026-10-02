from datetime import dt
class frist:
    def __init__(self):
        print("1 IS SAVING ACCOUNT")
        print("2 IS CURRENT ACCOUNT")

        n = int(input("Enter your choice : "))

        if n==1:
            a=20000
            print(a)
        elif n==2:
            a=30000
            print(a)
        else:
            print("Invalid Choice")
            exit()

        self.password = "yashvi123"
        self.transactions = []

    def login(self):
        cnt=1
        while cnt<=3:
            self.p=input("Enter password : ")

            if self.password==self.p:
                print("YOUR ACCOUNT IS OPEN SUCCESSFULLY..!")
                break
            else:
                cnt+=1
                if cnt<=3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()
    
    def withdraw():
       
        self.p=input("Enter password : ")

        if self.p==self.password:
            wid=int(input("Enter withdraw amount : "))

            if a-wid>=5000:
                a-=wid

                dt=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                transactions.append(
                    f"Withdraw  ₹{wid}  Balance: ₹{a}  {dt}"
                )


                print("WITHDRAW SUCCESSFUL")
                print("Balance =",a)
            else:
                print("Minimum balance ₹5000 required.")
        else:
            print("Wrong Password")
