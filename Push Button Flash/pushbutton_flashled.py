import RPi.GPIO as GPIO
from time import sleep
from time import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Ignore warning for now
button1=16
led=15

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW) 

estadoBotao = True
estAntBotao = True
estadoPisca = False

delay1 = 0
fast = 0

try:
    while True: # Run forever
        estadoBotao = GPIO.input(button1)
        
        if (not estadoBotao and estAntBotao):
            estadoPisca = not estadoPisca
            if estadoPisca == True:
                fast = fast + 50
                print("Led blinks every " + str(float((1050-fast)/1000)) + "s")
                
        estAntBotao = estadoBotao
        
        if estadoPisca:        
            if (int(time()*1000)- delay1) >= (1050 - fast):
                GPIO.output(led, GPIO.HIGH)

            if (int(time()*1000)- delay1) < (1050 - fast):
                GPIO.output(led, GPIO.LOW)
            
            if (int(time()*1000)- delay1) >= (2100 - fast * 2):
                delay1 = int(time()*1000)

        else:
            GPIO.output(led, GPIO.LOW)

finally:
    GPIO.output(led, GPIO.LOW)
    GPIO.cleanup()

