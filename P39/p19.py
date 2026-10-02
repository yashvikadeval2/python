f=open("library.txt","a")
while True:
    print("1. Book issue")
    print("2. Return book")
    print("3. Search book")
    print("4. Maintain books")
    print("5. Exit")

    n=int(input("Enter n : "))

    if n==1:
        no=int(input("Enter No. :"))
        name=input("Name : ")
        book=input("Book name :")
        date=input("Date of issue : ")
        if f.tell()==0:
            f.write(f"No\tName\t\t\tBook\t\t\tDate of issue")
        f.write(f"\n{no}\t{name}\t\t\t{book}\t\t\t{date}")

    elif n==2:
        f=open("library.txt","r")
        records=f.readlines()
        f.close()
        no=int(input("Enter No. to return: "))
        for i in range(len(records)):
            if records[i].split("\t")[0]==str(no):
                records.pop(i)
                break
        f=open("library.txt","w")
        f.writelines(records)
        f.close()

    elif n==3:
        f=open("library.txt","r")
        records=f.readlines()
        f.close()
        no=int(input("Enter No. to search: "))
        for i in range(len(records)):
            if records[i].split("\t")[0]==str(no):
                print(records[i])
                break

    elif n==4:
        f=open("library.txt","r")
        records=f.readlines()
        f.close()
        print("Current books in the library:")
        for record in records:
            print(record.strip())

    elif n==5:
        print("Thank you for visiting the library!")
        exit()

    else:
        print("Enter right number")   