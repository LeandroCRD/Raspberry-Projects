#Led Chaser - Turn On from 0 to 6 Leds and Turn Off from 6 to 0 Leds.

import RPi.GPIO as GPIO
import random
from time import sleep
from time import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # Ignore warning for now

dice = [14,15,17,18,22,23]

led1=dice[0]
led2=dice[1]
led3=dice[2]
led4=dice[3]
led5=dice[4]
led6=dice[5]

GPIO.setup(led1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led6, GPIO.OUT, initial=GPIO.LOW)

for i in range(6):
    
    for i in range(0,6):
        GPIO.output(dice[i], GPIO.HIGH)
        sleep(0.1)

    for i in range(5,-1,-1):
        GPIO.output(dice[i], GPIO.LOW)
        sleep(0.1)