#Simple count down timer
import time

my_time = int(input("Enter time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    days = int(x / 86400) 
    print(f"Day: {days} {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
print("TIMES UP!")
