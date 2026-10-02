f=open("student_management.txt","a")
while True:
    print("1. add record")
    print("2. Display record")
    print("3. Update record")
    print("4. Delete record")
    print("5. Search record")
    print("6. Exit")

    n=int(input("Enter n : "))

    if n==1:
        rn=int(input("Enter roll no. :"))
        name=input("Name : ")
        course=input("Course :")
        marks=int(input("Marks : "))
        att=int(input("Attendance : "))
        if f.tell()==0:
            f.write(f"Rn\tName\t\t\tCourse\t\t\tMarks\tAttendance")
        f.write(f"\n{rn}\t{name}\t\t{course}\t\t{marks}\t\t{att}")

    elif n==2:
        f=open("student_management.txt","r")
        print(f.read())
        # f.close()

    elif n==3:
        f=open("student_management.txt","r")
        records=f.readlines()
        f.close()
        rn=int(input("Enter roll no. to update: "))
        for i in range(len(records)):
            if records[i].split("\t")[0]==str(rn):
                name=input("Name : ")
                course=input("Course :")
                marks=int(input("Marks : "))
                att=int(input("Attendance : "))
                records[i]=f"{rn}\t{name}\t{course}\t\t\t{marks}\t\t{att}\n"
                break
        f=open("student_management.txt","w")
        f.writelines(records)
        f.close()

    elif n==4:
        f=open("student_management.txt","r")
        records=f.readlines()
        f.close()
        rn=int(input("Enter roll no. to delete: "))
        for i in range(len(records)):
            if records[i].split("\t")[0]==str(rn):
                records.pop(i)
                break
        f=open("student_management.txt","w")
        f.writelines(records)
        f.close()

    elif n==5:
        f=open("student_management.txt","r")
        records=f.readlines()
        f.close()
        rn=int(input("Enter roll no. to search: "))
        for i in range(len(records)):
            if records[i].split("\t")[0]==str(rn):
                print(records[i])
                break

    elif n==6:
        print("Thank you for visiting...")
        exit()

    else:
        print("enter right choice..")

# if f.tell()==0:
#     f.write(f"Rn\tName\tCourse\t\t\tMarks\tAttendance")
# f.write(f"\n{rn}\t{name}\t{course}\t\t\t{marks}\t\t{att}")