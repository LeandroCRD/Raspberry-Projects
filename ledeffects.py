## LIBRARIES ##
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
led = GPIO.PWM(14, 500)

## GUI DEFINITIONS ##
win = Tk()
win.title("LET'S PLAY WITH A LED")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## EVENT FUNCTIONS ##
def ledOnOff():
    if ledButton["text"] == 'LED OFF':
        led.stop(100)
        ledButton["text"] = 'LED ON'
    else:
        led.start(100)
        ledButton["text"] = 'LED OFF'

def blink():
    led.start(100)
    time.sleep(0.7)
    led.stop(100)

def pulse():

    led.start(0)

    for dc in range(0, 101, 5):
        led.ChangeDutyCycle(dc)
        time.sleep(0.1)
    for dc in range(100, -1, -5):
        led.ChangeDutyCycle(dc)
        time.sleep(0.1)

    led.stop(0)

def close():
    GPIO.cleanup()
    win.destroy()

## WIDGETS ##
ledButton = Button(win, text = 'LED ON', font = myFont, command = ledOnOff, bg = 'bisque2', height = 1, width = 24)
ledButton.grid(row=0,column=0)

blinkButton = Button(win, text = 'BLINK LED', font = myFont, command = blink, bg = 'bisque2', height = 1, width = 24)
blinkButton.grid(row=0,column=1)

pulseButton = Button(win, text = 'PULSE LED', font = myFont, command = pulse, bg = 'bisque2', height = 1, width = 24)
pulseButton.grid(row=0,column=2)

exitButton = Button(win, text = 'EXIT', font = myFont, command = close, bg = 'bisque2', height = 1, width = 79)
exitButton.grid(row=1, column=0, columnspan=3)

#EXIT CLEANLY
win.protocol("WM_DELETE_WINDOW", close) 

win.mainloop()

