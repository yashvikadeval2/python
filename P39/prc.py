
def display_students():
    try:
        with open("students.txt", "r") as file:
            print("\nStudent Records:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No student records found. Please add students first.")

def search_student():
    roll_number = input("Enter Roll Number to search: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_record = eval(line.strip())
                if student_record["roll_number"] == roll_number:
                    print("Student Record Found:")
                    print(student_record)
                    found = True
                    break
        if not found:
            print("Student record not found.")
    except FileNotFoundError:
        print("No student records found. Please add students first.")

def update_student():
    roll_number = input("Enter Roll Number to update: ")
    updated = False
    records = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_record = eval(line.strip())
                if student_record["roll_number"] == roll_number:
                    print("Current Record:", student_record)
                    student_record["name"] = input("Enter New Name: ")
                    student_record["course"] = input("Enter New Course: ")
                    student_record["marks"] = input("Enter New Marks: ")
                    student_record["attendance"] = input("Enter New Attendance: ")
                    updated = True
                records.append(student_record)

        if updated:
            with open("students.txt", "w") as file:
                for record in records:
                    file.write(str(record) + "\n")
            print("Student record updated successfully!")
        else:
            print("Student record not found.")
    except FileNotFoundError:
        print("No student records found. Please add students first.")

def delete_student():
    roll_number = input("Enter Roll Number to delete: ")
    deleted = False
    records = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_record = eval(line.strip())
                if student_record["roll_number"] == roll_number:
                    deleted = True
                    continue  
                records.append(student_record)

        if deleted:
            with open("students.txt", "w") as file:
                for record in records:
                    file.write(str(record) + "\n")
            print("Student record deleted successfully!")
        else:
            print("Student record not found.")
    except FileNotFoundError:
        print("No student records found. Please add students first.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()