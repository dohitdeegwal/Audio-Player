### Dohit Deegwal ###
#### 17-01-2022 ####

# dependencies
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename
import os.path
from pygame import mixer

# global variables
bg_default = ""
fg_default = ""
play_queue = []
playing_basename = ""
valid_extensions = (".mp3", ".wav")
mixer.init()

# window declaration

root = Tk()
root.geometry("700x350")
root.title("Audio Player")
#Make the window sticky for every case
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
# set window icon
def get_path(icon):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, icon)
    else:
        return icon
root.iconbitmap(get_path("icon.ico"))

# clears the labels
def clear_labels():
    lbl_filename.config(text="", bg=bg_default, fg=fg_default)
    lbl_playing.config(text="", bg=bg_default, fg=fg_default)
    lbl_validity.config(text="", bg=bg_default, fg=fg_default)

# gets the new file, validates it and updates the playlist
def chooseFile():
    lbl_filename.config(text="", bg=bg_default)
    lbl_validity.config(text="", bg=bg_default)

    global play_queue  # needed to modify global copies of variables
    filepath = askopenfilename()
    basename = os.path.basename(filepath)   
    extension = os.path.splitext(basename)[-1]
    
    if(not os.path.exists(filepath)):
        lbl_filename.config(text="Invalid Path!", bg="red")
    else:
        if extension not in valid_extensions:
            lbl_filename.config(text=basename, bg="red")          
            lbl_validity.config(text= "Unsupported File extension: " + extension + "\nChoose from: " + ", ".join(valid_extensions))
        else:
            play_queue.append(filepath)
            btn_play.config(state="normal")
            display_playlist()

# displays the playlist
def display_playlist():
    try:
        lbl_filename.config(text= "Up next: " + os.path.basename(play_queue[0]), bg = bg_default)
    except IndexError:
        lbl_filename.config(text= "Queue empty", bg = bg_default)
        btn_play.config(state="disabled")


# audio control functions

def play():
    global playing_basename, play_queue
    mixer.music.load(play_queue[0])
    mixer.music.play()
    playing_basename = os.path.basename(play_queue[0])

    btn_pause.config(text="Pause", command=pause, state="normal")
    btn_stop.config(state="normal")

    clear_labels()
    lbl_playing.config(text="Now Playing: " + playing_basename, bg="#00ff00")

    del(play_queue[0])
    display_playlist()

def pause():
    mixer.music.pause()
    clear_labels()
    display_playlist()
    lbl_playing.config(text="Paused: " + playing_basename, bg="orange")
    btn_pause.config(text="Resume", command=resume)

def resume():
    mixer.music.unpause()
    clear_labels()
    display_playlist()
    lbl_playing.config(text="Now Playing: " + playing_basename, bg="#00ff00")
    btn_pause.config(text="Pause", command=pause)

def stop():
    mixer.music.stop()
    clear_labels()
    display_playlist()
    btn_stop.config(state="disabled")
    btn_pause.config(text="Pause", state="disabled")
    
    lbl_playing.config(text="", bg=bg_default)


# widget declaration
lbl_title = Label(root, text="MP3 Player", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), bg="white", fg="Gray")

frame1 = LabelFrame(root)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(2, weight=1)
btn_choose = Button(frame1, text="Choose File", command=chooseFile)
lbl_playing = Label(frame1)
lbl_filename = Label(frame1)
lbl_validity = Label(frame1)

frame_buttons = LabelFrame(root, padx=5, pady=5)
frame_buttons.grid_rowconfigure(0, weight=1)
frame_buttons.grid_columnconfigure(2, weight=1)
btn_play = Button(frame_buttons, text="Play queued", state="disabled", command=play, width=10)
btn_stop = Button(frame_buttons, text="Stop", state="disabled", command=stop, width=10)
btn_pause = Button(frame_buttons, text="Pause", state="disabled", command=pause, width=10)

# widget packing
colspan_lbl = 6
colspan_btn = 2
lbl_title.grid(row=0, columnspan=colspan_lbl)

frame1.grid(row=1, column=0, columnspan=colspan_lbl, sticky=W+E, padx=10)
btn_choose.grid(row=1, column=2, columnspan=colspan_btn)
lbl_playing.grid(row=2, column=0, columnspan=colspan_lbl)
lbl_filename.grid(row=3, column=0, columnspan=colspan_lbl)
lbl_validity.grid(row=4, column=0, columnspan=colspan_lbl)

frame_buttons.grid(row=2, columnspan=colspan_lbl, sticky=W+E, padx=10, pady=10)
btn_play.grid(row=0, column=0, rowspan=2, columnspan=colspan_btn)
btn_pause.grid(row=0, column=2, rowspan=2, columnspan=colspan_btn)
btn_stop.grid(row=0, column=4, rowspan=2, columnspan=colspan_btn)

# get default widget colors
bg_default = lbl_validity.cget("bg")
fg_default = lbl_validity.cget("fg")

root.mainloop()