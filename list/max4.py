a=int(input("enter a = "))
b=int(input("enter b = "))
c=int(input("enter c = "))
d=int(input("enter d = "))

print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)

if a>b:
    if a>c:
        if a>d:
            print("a is max")
        else:
            print("d is max")
    else:
        if c>d:
            print("c is max")
        else:
            print("d is max")
else:
    if b>c:
        if b>d:
            print("b is max")
        else:
            print("d is max")
    else:
        if c>d:
            print("c is max")
        else:
            print("d is max")
        
        
    
        

