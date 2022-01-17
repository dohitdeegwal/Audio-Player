### Dohit Deegwal ###
#### 17-01-2022 ####

# dependencies
from tkinter import *
from tkinter.filedialog import askopenfilename
import os.path
from pygame import mixer

# global variables
default_bg = ""
play_queue = []
playing_basename = ""
valid_extensions = (".mp3", ".wav")
mixer.init()

# gets the new file, validates it and updates the playlist
def chooseFile():
    filename_lbl.config(text="Choosing file...", bg=default_bg)
    validity_lbl.config(text="", bg=default_bg)

    global play_queue  # needed to modify global copies of variables
    filepath = askopenfilename()
    basename = os.path.basename(filepath)   
    extension = os.path.splitext(basename)[1]
    
    if(not os.path.exists(filepath)):
        filename_lbl.config(text="Invalid Path!", bg="red")
    else:
        if extension not in valid_extensions:
            filename_lbl.config(text=basename, bg="red")          
            validity_lbl.config(text= "Unsupported File extension: " + extension + "\nChoose from: " + ", ".join(valid_extensions))
        else:
            play_queue.append(filepath)
            filename_lbl.config(text="Up next: " + os.path.basename(play_queue[0]))
            play_btn.config(state="normal")


# audio control functions

def play():
    global playing_basename, play_queue
    mixer.music.load(play_queue[0])
    mixer.music.play()
    playing_basename = os.path.basename(play_queue[0])

    pause_btn.config(text="Pause", command=pause, state="normal")
    stop_btn.config(state="normal")

    playing_lbl.config(text="Now Playing: " + playing_basename, bg="green")

    try:
        filename_lbl.config(text= "Up next: " + os.path.basename(play_queue[1]))
    except IndexError:
        filename_lbl.config(text= "Queue empty")
        play_btn.config(state="disabled")

    del(play_queue[0])

def pause():
    mixer.music.pause()
    playing_lbl.config(text="Paused: " + playing_basename)
    pause_btn.config(text="Resume", command=resume)

def resume():
    mixer.music.unpause()
    playing_lbl.config(text="Now Playing: " + playing_basename)
    pause_btn.config(text="Pause", command=pause)

def stop():
    mixer.music.stop()
    stop_btn.config(state="disabled")
    pause_btn.config(text="Pause", state="disabled")
    play_btn.config(text="Play queued", command=play)
    playing_lbl.config(text="", bg=default_bg)


# window declaration
window = Tk()
window.title("Audio Player")

# widget declaration
title = Label(window, text="MP3 Player", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), bg="white", fg="Gray")
choose_btn = Button(master=window, text="Choose File", command=chooseFile)
playing_lbl = Label(window)
filename_lbl = Label(window)
validity_lbl = Label(window)
play_btn = Button(window, text="Play queued", state="disabled", command=play, width=10)
stop_btn = Button(window, text="Stop", state="disabled", command=stop, width=10)
pause_btn = Button(window, text="Pause", state="disabled", command=pause, width=10)

# widget packing
lbl_colspan = 6
btn_colspan = 2
title.grid(row=0, columnspan=lbl_colspan)
choose_btn.grid(row=1, column=2, columnspan=btn_colspan)
playing_lbl.grid(row=2, column=0, columnspan=lbl_colspan)
filename_lbl.grid(row=3, column=0, columnspan=lbl_colspan)
validity_lbl.grid(row=4, column=0, columnspan=lbl_colspan)
play_btn.grid(row=5, column=0, rowspan=2, columnspan=btn_colspan)
pause_btn.grid(row=5, column=2, rowspan=2, columnspan=btn_colspan)
stop_btn.grid(row=5, column=4, rowspan=2, columnspan=btn_colspan)

# get default widget bg color
default_bg = validity_lbl.cget('bg')

window.mainloop()