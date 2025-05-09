import datetime
import time
import webbrowser


time_alarm = input("enter the time : ")
print (f"alarm is set for {time_alarm} ")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    if(current_time == time_alarm):
        webbrowser.open("https://www.youtube.com/watch?v=2vjPBrBU-TM")
        break
    time.sleep(1)        
