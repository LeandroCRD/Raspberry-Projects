from time import sleep # Import the sleep function from the time module
from os import system, name # Import the system and name module

def clear(): # Function to clean screen
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear') 

#Print something and call Clear function
sleep(2)
print("Hello")
sleep(2)
print("Who are you?")
sleep(2)
clear()
sleep(2)
