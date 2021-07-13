import time
import datetime
from tkinter import *
from playsound import playsound

root = Tk()
root.title("Alarm Clock")
root.geometry("359x150+0+0")
root.configure(background="black")

alarmH = int(input("What hour do you want to wake up? "))
alarmM = int(input("What minute do you want to wake up? "))

def start():
    text = time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(200,start)

label = Label(root,font=("ds-digital",50,'bold'),bg='black', fg='red',bd=50)
label.grid (row=0,column=1)
start()
root.mainloop()

while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and 
       alarmM == datetime.datetime.now().minute):
       playsound('/Users/Kanta Garg/Desktop/SATISH/Projects/Alarm-Clock/lalala.mp3')
       break