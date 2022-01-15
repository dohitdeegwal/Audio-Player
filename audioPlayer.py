### Dohit Deegwal ###
#### 15-01-2022 ####

from tkinter import *
from tkinter.filedialog import askopenfilename
import os.path
from pygame import mixer

# global variables
filepath = ""
default_bg = ""
valid_extensions = (".mp3", ".wav")

# set the initial button and label states
def initialize():
    filename_lbl.config(text="Choosing file...", bg=default_bg)
    validity_lbl.config(text="", bg=default_bg)
    act_btn.config(state="disabled", command=play)
    stop_btn.config(state="disabled")

# gets the filepath and checks for valid extension
def chooseFile():
    initialize()
    global filepath  # needed to modify global copy of filepath
    filepath = askopenfilename()
    filename_lbl.config(text=os.path.basename(filepath))

    if(not os.path.exists(filepath)):
        filename_lbl.config(text="Invalid Path!" + filepath, bg="red")
    else:
        extension = os.path.splitext(filepath)[1]
        if extension not in valid_extensions:
            filename_lbl.config(bg="red")
            lbl_text = "Unsupported File extension: " + extension + \
                "\nChoose from: " + ", ".join(valid_extensions)
            validity_lbl.config(text=lbl_text)
        else:
            filename_lbl.config(bg="green")
            act_btn.config(state="normal")
            mixer.init()
            mixer.music.load(filepath)


# audio control functions

def resume():
    mixer.music.unpause()
    act_btn.config(text="Pause", command=pause)


def pause():
    mixer.music.pause()
    act_btn.config(text="Resume", command=resume)


def play():
    mixer.music.play()
    act_btn.config(text="Pause", command=pause)
    stop_btn.config(state="normal")


def stop():
    mixer.music.stop()
    stop_btn.config(state="disabled")
    act_btn.config(text="Play", command=play)

# window declaration
window = Tk()
window.title("Audio Player")

# widget declaration
title = Label(window, text="MP3 Player", bd=9, relief=GROOVE, font=(
    "times new roman", 50, "bold"), bg="white", fg="Gray")
choose_btn = Button(master=window, text="Choose File", command=chooseFile)
filename_lbl = Label(window)
validity_lbl = Label(window)
act_btn = Button(window, text="Play", state="disabled", command=play, width=10)
stop_btn = Button(window, text="Stop", state="disabled",command=stop, width=10)

# widget packing
title.grid(row=0, columnspan=5)
choose_btn.grid(row=1, column=2)
filename_lbl.grid(row=2, column=0, columnspan=5)
validity_lbl.grid(row=3, column=0, columnspan=5)
act_btn.grid(row=4, column=0, rowspan=2, columnspan=2)
stop_btn.grid(row=4, column=3, rowspan=2, columnspan=2)

# get default widget bg color
default_bg = validity_lbl.cget('bg')

window.mainloop()