from tkinter import *
import datetime
import time
from threading import *
import subprocess
import sys
import os

# Creating Object using Tkinter
clock = Tk()
 
# Set geometry of the alarm clock
clock.geometry("450x250")

# Use Threading for the clock
def Threading():
    al=Thread(target=alarmclock)
    al.start()
 
def alarmclock():

    setAlarmButton.config(state="disabled")

    set_alarm = "Alarm set successfully"
    alarmSetlabel = Label(clock,text=set_alarm,font=("Helvetica 15 bold"))
    alarmSetlabel.pack()
    disableAlarmButton.config(state="normal")
    
    
    while True:
        # Set Alarm
        set_alarm_time = f"{hr.get()}:{min.get()}:{sec.get()}"
 
        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        # print(current_time,set_alarm_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            clock.after(1, alarmSetlabel.destroy)
            wakeUpLabel = Label(clock,text="Time to Wake up",font=("Helvetica 15 bold"))
            wakeUpLabel.pack()
            for i in range(5):
                sound = subprocess.call(["afplay", "perfect.mp3"])
            clock.after(1, wakeUpLabel.destroy)
            setAlarmButton.config(state="normal")
            disableAlarmButton.config(state="disabled")
            return None

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
                                    
# Add Labels, Frame, Button, Optionmenus
Label(clock,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(clock,text="Set Time",font=("Helvetica 15 bold")).pack()
 
design = Frame(clock)
design.pack()
 
hr = StringVar(clock)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23'
        )
hr.set(hours[0])
 
hrs = OptionMenu(design, hr, *hours)
hrs.pack(side=LEFT)
 
min = StringVar(clock)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
min.set(minutes[0])
 
mins = OptionMenu(design, min, *minutes)
mins.pack(side=LEFT)
 
sec = StringVar(clock)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
sec.set(seconds[0])
 
secs = OptionMenu(design, sec, *seconds)
secs.pack(side=LEFT)
 
SetAlarm = "Set Alarm"

buttonFrame = Frame(clock)
buttonFrame.pack()
setAlarmButton = Button(buttonFrame,text=SetAlarm,font=("Helvetica 15"),command=Threading)
setAlarmButton.pack(pady=20, side=LEFT)
disableAlarmButton = Button(buttonFrame,text="Stop",font=("Helvetica 15"),command=restart_program)
disableAlarmButton.pack(pady=20)
disableAlarmButton.config(state="disabled")

# Execute Tkinter
clock.mainloop()
