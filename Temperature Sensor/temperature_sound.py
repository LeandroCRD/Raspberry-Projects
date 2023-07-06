import os # Import operating system functions module
import time # Import the time module
    
while True:
    # Check and Print the current temperature of the Raspeberry
    temp = os.popen("vcgencmd measure_temp -n").readline()  
    txt = temp.replace("temp=","")
    txt2 = txt.replace("'C","")
    e = float(txt2)
    print("Temperature: "+ str(e) + "'C")
    
    # If temperature is >70 print Carefull message and play sound
    if e > 70:
        print("Carefull!")
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Python Projects/mariocoin.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    time.sleep(10)
    
