#Led Dice - Press a Button to Randomly Turn Leds from 1 to 6.

import RPi.GPIO as GPIO
from time import sleep
from time import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # Ignore warning for now

button=4

dice = [14,15,17,18,22,23]

led1=dice[0]
led2=dice[1]
led3=dice[2]
led4=dice[3]
led5=dice[4]
led6=dice[5]

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led6, GPIO.OUT, initial=GPIO.LOW)

estadoBotao = True
estAntBotao = True

working = False

try:
    while True:
        estadoBotao = GPIO.input(button)

        if (not estadoBotao and estAntBotao):
            working = True
            for i in range(6):
                GPIO.output(dice[i], GPIO.LOW)
        
        if working == True:
            #for i in dice:
            for i in range(100):
                OnOff = dice[random.randint(0, 5)]
                GPIO.output(OnOff, GPIO.HIGH)
                sleep(0.015)
                GPIO.output(OnOff, GPIO.LOW)
            
            sleep(0.8)

            draw = random.randint(1, 6)
            for i in range(draw):
                GPIO.output(dice[i], GPIO.HIGH)
            print('Number ' + str(draw))
            sleep(5)
            working = False
        
        else:
            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led2, GPIO.LOW)
            GPIO.output(led3, GPIO.LOW)
            GPIO.output(led4, GPIO.LOW)
            GPIO.output(led5, GPIO.LOW)
            GPIO.output(led6, GPIO.LOW)

finally:
    for i in range(0,6):
        GPIO.output(dice[i], GPIO.LOW)
        GPIO.cleanup()