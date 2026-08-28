#Creating simple alarm clock
import time
import datetime
import subprocess

def setAlarm(alarmTime):
    print(f"Alarm set for {alarmTime}")
    soundFile = "nowyouwontletgo.mp3"
    isRunning = True
    
    while isRunning:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currentTime)
        
        if currentTime == alarmTime:
            print("Wake Up!")
            subprocess.run(["cmd", "/c", "start", "", soundFile])
            isRunning = False
        
        time.sleep(1)
        
        
    
if __name__ == "__main__":
    alarmTimer = input("Enter the alarm time: (HH:MM:SS)")
    setAlarm(alarmTimer)
    
