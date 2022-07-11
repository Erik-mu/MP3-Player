from tkinter import *
from tkinter import filedialog as fd
import vlc
import eyed3
import os


def open():
    global filename
    filename = fd.askopenfilename(title="select", filetypes=[("music)", ".mp3")])   #only mp3

def play():
    global media
    media = vlc.MediaPlayer(filename)
    media.play()
    audio = eyed3.load(filename)
    # artist = audio.tag.artist
    # artist_.config(text=artist)
    # title = audio.tag.title
    # title_.config(text=title)
    duration = time(audio.info.time_secs)
    duration_.config(text=duration)
    name = os.path.basename(filename)
    name_.config(text=name)


def stop():
    media.stop()

def pause():
    media.pause()

def time(s):
    s = int(s)
    m,s = divmod(s, 60)
    time_total = f"{m:02d}:{s:02d}"
    return time_total

window = Tk()
window.title("MP3 Player")
window.geometry("600x120")
window.config(bg="#2C3639")
open_button = Button(text="Open", command=open, bg="#3F4E4F", fg="#A27B5C", width=20).grid(column=0, row=1)
play_button = Button(text="Play", command=play, bg="#3F4E4F", fg="#A27B5C", width=20).grid(column=1, row=1)
stop_button = Button(text="Stop", command=stop, bg="#3F4E4F", fg="#A27B5C", width=20).grid(column=2, row=1)
pause_button = Button(text="Pause", command=pause, bg="#3F4E4F", fg="#A27B5C",width=20 ).grid(column=3, row=1)

# artist_ = Label(text="")
# artist_.grid(column=0, row=2)
# title_ = Label(text="")
# title_.grid(column=1, row=2)
duration_ = Label(text="", bg="#2C3639",fg="#DCD7C9")
duration_.grid(column=3, row=3)


now = Label(text="Now playing: ", bg="#2C3639", fg="#DCD7C9").grid(column=0, row=3)
name_ = Label(text="",bg="#2C3639",fg="#DCD7C9")
name_.grid(column=1, row=3, columnspan=2)
window.mainloop()
