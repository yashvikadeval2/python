#. A Number System Conversion Program is a Python program used to convert numbers from one number system to another, such as binary, decimal, octal, and hexadecimal.
print("1.binary to decimal")
print("2.binary to octal")
print("3.binary to hexadecimal")
print("4.demial to binary")
print("5.decimal to octal")
print("6.decimal to hexadecimal")
print("7.octal to binary")
print("8.octal to decimal")
print("9.octal to hexadecimal")
print("10.hexadecimal to binary")
print("11.hexadecimal to decimal")
print("12.hexadecimal to octal")

ch=int(input("enter your choice:"))

match ch:
    case 1:
        n = input("Enter a binary number: ")
        print("Decimal number is:", int(n, 2))

    case 2:
        n=input("enter a binary number:")
        print("octal number is:",oct(int(n,2)))

    case 3:
        n=input("enter a binary number:")
        print("hexadecimal number is:",hex(int(n,2)))

    case 4:
        n=int(input("enter a decimal number:"))
        print("binary number is:",bin(n))

    case 5:
        n=int(input("enter a decimal number:"))
        print("octal number is:",oct(n))

    case 6:
        n=int(input("enter a decimal number:"))
        print("hexadecimal number is:",hex(n))

    case 7:
        n=input("enter a octal number:")
        print("binary number is:",bin(int(n,8)))

    case 8:
        n=input("enter a octal number:")
        print("decimal number is:",int(n,8))

    case 9:
        n=input("enter a octal number:")
        print("hexadecimal number is:",hex(int(n,8)))

    case 10:
        n=input("enter a hexadecimal number:")
        print("binary number is:",bin(int(n,16)))

    case 11:
        n=input("enter a hexadecimal number:")
        print("decimal number is:",int(n,16))

    case 12:
        n=input("enter a hexadecimal number:")
        print("octal number is:",oct(int(n,16)))

    case _:
        print("invalid choice")
        