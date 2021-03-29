from tkinter import *
import RPi.GPIO as GPIO
from time import sleep
from time import time

"""Setup the GPIO Pins"""
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

log = ""

def buttonPressed(channel):
    """This function should be called when GPIO 16 has a rising edge event"""
    global log
    if str(log[-2:]) != str(99):
        GPIO.output(15, GPIO.LOW)
        var.set(var.get() + 1)
        sleep(0.25)
        
"""Register the callback"""
GPIO.add_event_detect(16, GPIO.RISING, callback=buttonPressed)

root = Tk()

root.geometry("172x115+1650+37")
root.resizable(False,False)
root.configure(background="black")
root.overrideredirect(1)

var = IntVar() # instantiate the IntVar variable class
var.set(0) # set it to 0 as the initial value
 
#x = var[-2:]
# the label's textvariable is set to the variable class instance
label1=Label(root,font=("alarm clock",60,"bold"),textvariable=var, bd=0,bg='black', fg="red", padx=0, pady=0)
label1.grid(row=2,column=1, columnspan=2,ipadx=15, ipady=0)

button1=Button(root,text="Click", width=7,borderwidth=2)
button1.grid(row=1,column=1,sticky='W',pady=0)
button2=Button(root,text="Reset", width=7,borderwidth=2)
button2.grid(row=1,column=2,sticky='W')

root.mainloop()