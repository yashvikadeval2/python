unit=int(input("enter unit = "))

if unit<=50:
    bill=unit*1
elif unit>50 and unit<=100:
    bill=50*1+(unit-50)*2
elif unit>100 and unit<=200:
    bill=(50*1)+(50*2)+(unit-100)*3
elif unit>200 and unit<=400:
    bill=(50*1)+(50*2)+(100*3)+(unit-200)*4
else:
    bill=(50*1)+(50*2)+(100*3)+(200*4)+(unit-400)*5
    
bill=bill+(bill/10)
    


print("bill = ",bill)
