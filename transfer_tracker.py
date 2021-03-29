import time
from time import sleep

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from playsound import playsound
import os
from os import system, name

def clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear') 

from colored import fg, bg, attr

colort = fg(154)
colorc = fg(2)
colorm = fg(1)

reset = attr('reset')
clear()
class Watcher:
    DIRECTORY_TO_WATCH = "/media/NASHDD1/torrent-complete"

    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)

        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")
        
        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):       
            import os
            import shutil
            extensions = [".mp4",".avi",".mkv"]
            sourcepath='/media/NASHDD1/torrent-complete'
            sourcefiles = os.listdir(sourcepath)
            destinationpath = '/media/NASHDD1/Movies'
            for root, dirs, files in os.walk("/media/NASHDD1/torrent-complete"):
                for file in files:
                    if file.endswith(tuple(extensions)):
                        shutil.move(os.path.join(root,file), os.path.join(destinationpath,file))
                        print(colorc + "***Transfer Completed***" + reset)
                    
                        from datetime import date
                        from datetime import datetime
                        # datetime object containing current date and time
                        now = datetime.now()
                        
                        # dd/mm/YY H:M:S
                        dt_string = now.strftime("%d/%m/%Y")
                        dt_string2 = now.strftime("%H:%M:%S")
                        print"Date:", dt_string,"Time:", dt_string2

                        t=event.src_path
                        base=os.path.basename(t)
                        print(os.path.join(file))

                        from os import environ
                        import pygame
                        pygame.mixer.init()
                        pygame.mixer.music.load("/home/pi/Documents/Python Projects/mariocoin.wav")
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy() == True:
                            continue
                        print("\n")

if __name__ == '__main__':
    w = Watcher()
    w.run()
