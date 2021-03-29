#INSTALL pip3 install gTTS pyttsx3 playsound

import pandas as pd
import csv
from datetime import date
from time import sleep

#PICK DATE OF THE DAY AND FORMAT IT (DD/MM/YY)
today = date.today()
d1 = today.strftime("%d/%m/%Y")

#OPEN CSV DATABASE FILE 
df = pd.read_csv("/home/pi/Documents/Python Projects/Agenda/robot_agenda_booking.csv")

#CHECK IF DATE OF THE DAY IS IN CSV DATABASE FILE
df1 = df.loc[df["Date"].str.contains(d1)]

if df1.empty:
    x = "Empty"
else:
    x = "Filled"
    df2 = df1.iloc[0]
    df3 = df2.drop(columns = ["Task"])
    df4 = df3.iloc[0]
    d2 = str(df2[1])
    df5 = df2.drop(columns = ["Date"])
    df6 = df5.iloc[0]

import gtts
tts = gtts.gTTS("Goodmorning!")
tts.save("/home/pi/Documents/Python Projects/Agenda/Goodmorning.mp3")
tts = gtts.gTTS("Today is the " + d1 + ".")
tts.save("/home/pi/Documents/Python Projects/Agenda/Today.mp3")

import pygame
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Documents/Python Projects/Agenda/Goodmorning.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Documents/Python Projects/Agenda/Today.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

sleep(1)

if x == "Filled":
    tts = gtts.gTTS("You have today the following booking.")
    tts.save("/home/pi/Documents/Python Projects/Agenda/Appointment1.mp3")
    tts = gtts.gTTS(d2)
    tts.save("/home/pi/Documents/Python Projects/Agenda/Appointment2.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Documents/Python Projects/Agenda/Appointment1.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

    sleep(0.5)

    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Documents/Python Projects/Agenda/Appointment2.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("Today is: " + d1 + "\nYou have the following booking: " + d2 + "\n")

else:
    tts = gtts.gTTS("You don't have any appointment today.")
    tts.save("/home/pi/Documents/Python Projects/Agenda/NoAppointment1.mp3")
    tts = gtts.gTTS("Have a Nice Day!")
    tts.save("/home/pi/Documents/Python Projects/Agenda/NoAppointment2.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Documents/Python Projects/Agenda/NoAppointment1.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

    sleep(0.5)

    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Documents/Python Projects/Agenda/NoAppointment2.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("Today is: " + d1 + "\nYou don't have any apointment today.\n")