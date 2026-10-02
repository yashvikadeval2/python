# A Number System Conversion Program is a Python program used to convert numbers from one number system to another, such as binary, decimal, octal, and hexadecimal.

from unittest import case

import numpy as np
n=input("Enter the conversion type ""(\n1.decimal to binary, \n2.decimal to octal, \n3.decimal to hexadecimal, \n4.binary to decimal, \n5.octal to decimal, \n6.hexadecimal to decimal, \n7.hexadecimal to binary, \n8.hexadecimal to octal, \n9.octal to binary, \n10.octal to hexadecimal, \n11.binary to octal, \n12.binary to hexadecimal): "):
match n:
    case "1":
        decimal = int(input("Enter a decimal number: "))
        print(f"Binary: {np.binary_repr(decimal)}")

    case "2":
        decimal = int(input("Enter a decimal number: "))
        print(f"Octal: {np.base_repr(decimal, base=8)}")

    case "3":
        decimal = int(input("Enter a decimal number: "))
        print(f"Hexadecimal: {np.base_repr(decimal, base=16)}")

    case "4":
        binary = input("Enter a binary number: ")   
        decimal = int(binary, 2)
        print(f"Decimal: {decimal}")

    case "5":
        octal = input("Enter an octal number: ")
        decimal = int(octal, 8)
        print(f"Decimal: {decimal}")

    case "6":
        hexadecimal = input("Enter a hexadecimal number: ")
        decimal = int(hexadecimal, 16)
        print(f"Decimal: {decimal}")

    case "7":
        hexadecimal = input("Enter a hexadecimal number: ")
        decimal = int(hexadecimal, 16)
        print(f"Binary: {np.binary_repr(decimal)}")

    case "8":
        hexadecimal = input("Enter a hexadecimal number: ")
        decimal = int(hexadecimal, 16)
        print(f"Octal: {np.base_repr(decimal, base=8)}")

    case "9":
        octal = input("Enter an octal number: ")
        decimal = int(octal, 8)
        print(f"Binary: {np.binary_repr(decimal)}")

    case "10":
        octal = input("Enter an octal number: ")
        decimal = int(octal, 8)
        print(f"Hexadecimal: {np.base_repr(decimal, base=16)}")

    case "11":
        binary = input("Enter a binary number: ")
        decimal = int(binary, 2)
        print(f"Octal: {np.base_repr(decimal, base=8)}")

    case "12":
        binary = input("Enter a binary number: ")
        decimal = int(binary, 2)
        print(f"Hexadecimal: {np.base_repr(decimal, base=16)}")



