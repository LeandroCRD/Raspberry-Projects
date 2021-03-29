import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

a = input("Quantos nos tens?\n")

if a > 21:
    print("Green Light")
    for n in range(10):
         GPIO.output(8, GPIO.HIGH) # Turn on
         sleep(0.5) # Sleep for 1 second
         GPIO.output(8, GPIO.LOW) # Turn off
         sleep(0.25) # Sleep for 1 second
else:
    print("Red Light")
    for n in range(10):
         GPIO.output(7, GPIO.HIGH) # Turn on
         sleep(0.5) # Sleep for 1 second
         GPIO.output(7, GPIO.LOW) # Turn off
         sleep(0.25) # Sleep for 1 second


 