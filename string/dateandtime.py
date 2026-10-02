import datetime as dt

d=dt.datetime.now()
# print('data=',d)


# cd=d.date()
# print('data=',cd)

# ct=d.time()
# print('current_time=',ct)

# print("current date time=",d)

# date = d.strftime("%d/%m/%Y")
# print('Date String:', date)

# time = d.strftime("%H:%M:%S")
# print('Time String:', time)

# year = d.strftime("%Y")
# print('Year String:', year)

# month = d.strftime("%m")
# print('Month String:', month)

# day = d.strftime("%d")
# print('Day String:', day)

print('Current Time:',d)
print("Time in 24 hours format:", d.strftime("%H-%M-%S"))
print("Time in 12 hours format:", d.strftime("%I-%M-%S"))