# simple yt dl gui
import os
import sys
import subprocess
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar

# Base Window
root = tk.Tk()
root.title('yt-playlist-downloader by cole')
root.geometry("500x200")

# Entry Field
enterF = Entry(root, width=50, font=('Helvetica', 24))
enterF.pack()

progressB = ttk.Progressbar(root, orient=HORIZONTAL,
                            length=100, mode='determinate')
progressB.pack()

# Click Action: Download Playlist


def myClick():
    play = str(enterF.get())
    # Downloads Playlist: Checks if songs alreday downloaded. Extracts only mp3
    p = subprocess.run(["youtube-dl", "--download-archive", "context.txt",
                        "--extract-audio", "--audio-format", "mp3", play])
    # while subrpocess running do loading bar ? TODO: HERE
    myLabel = Label(root, text="download complete")
    enterF.delete(0, 'end')
    myLabel.pack()


# Button
myButton = Button(root, text="Press Here To Download", command=myClick)
myButton.pack()
root.mainloop()
# WORKS:
# subprocess.run(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "https://www.youtube.com/playlist?list=PLuWUqfdJLtimhQsZrsnTrDUO9BWVmE5_9"])
