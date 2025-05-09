import datetime
import time
import webbrowser


time = input("enter the time : ")
print (f"alarm is set for {time} ")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    if(current_time != time):
        continue
    else:
        webbrowser.open("https://www.youtube.com/watch?v=2vjPBrBU-TM")
        break