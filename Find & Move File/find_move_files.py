#Find and Move from a Source Path specific Extensions to a specific Destination Path
import os
import shutil
extensions = [".mp4",".avi",".mkv"]
sourcepath='/media/NASHDD1/torrent-complete'
sourcefiles = os.listdir(sourcepath)
destinationpath = '/media/NASHDD1/Movies'
for root, dirs, files in os.walk("/media/NASHDD1/torrent-complete"):
    for file in files:
        if file.endswith(tuple(extensions)):
             print(os.path.join(file))
             shutil.move(os.path.join(root,file), os.path.join(destinationpath,file))
             
             
             
