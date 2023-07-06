import pygame # Import pygame module

#Play a sound from a specific folder
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Documents/Python Projects/mariocoin.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
