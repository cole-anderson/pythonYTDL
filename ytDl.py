#simple yt dl gui
import os
import sys
import subprocess
from tkinter import *
import tkinter as tk

root = tk.Tk()

e = Entry(root, width=50, font=('Helvetica', 24))
e.pack()

def myClick():
    play = str(e.get())
    subprocess.run(["youtube-dl", "--download-archive", "context.txt", "--extract-audio", "--audio-format", "mp3", play])
    myLabel = Label(root, text="download complete")
    e.delete(0, 'end')
    myLabel.pack()
    
myButton = Button(root, text="Press Here To Download", command=myClick)
myButton.pack()
root.mainloop()
# WORKS:
# subprocess.run(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "https://www.youtube.com/playlist?list=PLuWUqfdJLtimhQsZrsnTrDUO9BWVmE5_9"])

