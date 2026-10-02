
print("1. fahenheit -> degrees celsius")
print("2. fahenheit -> kelvin")
print("3. kelvin -> degrees celsius")
print("4. kelvin -> fahrenheit")
print("5. degrees celsius -> fahenheit") 
print("6. degrees celsius -> kelvin")


conversion=input("Enter the conversion choose (1 to 6): ")

if conversion=="1":
    fahrenheit=float(input("Enter temperature in Fahrenheit: "))
    celsius=(fahrenheit-32)*5/9
    print("Temperature in Celsius:",celsius)

elif conversion=="2":
    fahrenheit=float(input("Enter temperature in Fahrenheit: "))
    kelvin=(fahrenheit-32)*5/9+273.15
    print("Temperature in Kelvin:",kelvin)

elif conversion=="3":
    kelvin=float(input("Enter temperature in Kelvin: "))
    celsius=kelvin-273.15
    print("Temperature in Celsius:",celsius)
    
elif conversion=="4":
    kelvin=float(input("Enter temperature in Kelvin: "))
    fahrenheit=(kelvin-273.15)*9/5+32
    print("Temperature in Fahrenheit:",fahrenheit)

elif conversion=="5":
    celsius=float(input("Enter temperature in Celsius: "))
    fahrenheit=(celsius*9/5)+32
    print("Temperature in Fahrenheit:",fahrenheit)

elif conversion=="6":
    celsius=float(input("Enter temperature in Celsius: "))
    kelvin=celsius+273.15
    print("Temperature in Kelvin:",kelvin)
    
else:
    print("Invalid conversion.")





