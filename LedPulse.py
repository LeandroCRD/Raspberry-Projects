import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

led = GPIO.PWM(14, 500)

led.start(0)

while(1):
for dc in range(0, 100, 5):
    led.ChangeDutyCycle(dc)
    time.sleep(0.1)
for dc in range(100, -1, -5):
    led.ChangeDutyCycle(dc)
    time.sleep(0.1)

#OTHER WAY TO PULSE A LED

#from gpiozero import PWMLED
#from signal import pause

#led = PWMLED(14)

#led.pulse()

#pause()
