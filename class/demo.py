# Account Choice

while True:
    print("1 IS SAVING ACCOUNT")
    print("2 IS CURRENT ACCOUNT")

    n = int(input("Enter your choice : "))

    if n == 1:
        a = 20000
        print("Saving Account Balance =", a)
        break

    elif n == 2:
        a = 30000
        print("Current Account Balance =", a)
        break

    else:
        print("Invalid Choice! Please enter 1 or 2.\n")


# Password Creation

# while True:
#     password = input("Create Password : ")

#     has_alpha = False
#     has_digit = False

#     for ch in password:
#         if ch.isalpha():
#             has_alpha = True
#         if ch.isdigit():
#             has_digit = True

#     if has_alpha and has_digit:
#         print("Password Created Successfully!")
#         break
#     else:
#         print("Password must contain at least one alphabet and one digit.\n")

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


# Login

cnt = 1
while cnt <= 3:
    p = input("Enter Password : ")

    if p == password:
        print("YOUR ACCOUNT IS OPEN SUCCESSFULLY..!")
        break
    else:
        cnt += 1

        if cnt <= 3:
            print("WRONG PASSWORD...")
        else:
            print("EXIT")