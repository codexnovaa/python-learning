# Working with date and time

import datetime

date = datetime.date(2026, 8, 2)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m/%d/%Y ")

print(now)

targetDateTime = datetime.datetime(2026, 1, 2, 12, 30, 1)
currentDateTime = datetime.datetime.now()

if targetDateTime < currentDateTime:
    print("Target datetime has passed")
else:
    print("Target datetime still has not passed")
