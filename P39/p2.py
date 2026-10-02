#2. Convert kilometers to miles.


print("Distance Unit Converter")
print("1. Kilometers to Meters")
print("2. Kilometers to Centimeters")
print("3. Kilometers to Miles")
print("4. Meters to Kilometers")
print("5. Meters to Centimeters")
print("6. Meters to Miles")
print("7. Centimeters to Kilometers")
print("8. Centimeters to Meters")
print("9. Centimeters to Miles")
print("10. Miles to Kilometers")
print("11. Miles to Meters")
print("12. Miles to Centimeters")

c = int(input("Enter your c (1-12): "))
n = float(input("Enter the n: "))

if c==1:
    print("Meters=",n*1000)

elif c==2:
    print("Centimeters=",n*100000)

elif c==3:
    print("Miles=",n*0.621371)

elif c==4:
    print("Kilometers=",n/1000)

elif c==5:
    print("Centimeters=",n*100)

elif c==6:
    print("Miles=",n/1609.34)

elif c==7:
    print("Kilometers=",n/100000)

elif c==8:
    print("Meters=",n/100)

elif c==9:
    print("Miles=",n/160934.4)

elif c==10:
    print("Kilometers=",n*1.60934)

elif c==11:
    print("Meters=",n*1609.34)

elif c==12:
    print("Centimeters=",n*160934.4)

else:
    print("Invalid choice")