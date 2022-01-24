### Dohit Deegwal ###

# dependencies
from tkinter.filedialog import askopenfilename
from pygame import mixer
from frontend import *

# global variables
play_queue = []
playing_basename = ""
valid_extensions = (".mp3", ".wav")
mixer.init()

# clears the labels
def clear_labels():
    lbl_queue.configure(text="", bg=bg_default, fg=fg_default)
    lbl_playing.configure(text="", bg=bg_default, fg=fg_default)

# gets the new file, validates it and updates the playlist
def chooseFile():
    display_playlist()

    global play_queue  # needed to modify global copies of variables
    filepath = askopenfilename(title="Select a file", filetypes=(("Supported audio files", valid_extensions),))
    if(os.path.exists(filepath)):
        play_queue.append(filepath)
        btn_play.configure(state="normal")
        
    display_playlist()
        

# displays the playlist
def display_playlist():
    try:
        lbl_queue.configure(text= "Up next: " + os.path.basename(play_queue[0]), bg = bg_default)
    except IndexError:
        lbl_queue.configure(text= "Queue empty", bg = bg_default)
        btn_play.configure(state="disabled")


# audio control functions

def play():
    global playing_basename, play_queue
    mixer.music.load(play_queue[0])
    mixer.music.play()
    playing_basename = os.path.basename(play_queue[0])

    btn_pause.configure(text="Pause", command=pause, state="normal")
    btn_stop.configure(state="normal")

    clear_labels()
    lbl_playing.configure(text="Now Playing: " + playing_basename, bg="#00ff00")

    del(play_queue[0])
    display_playlist()

def pause():
    mixer.music.pause()
    clear_labels()
    display_playlist()
    lbl_playing.configure(text="Paused: " + playing_basename, bg="orange")
    btn_pause.configure(text="Resume", command=resume)

def resume():
    mixer.music.unpause()
    clear_labels()
    display_playlist()
    lbl_playing.configure(text="Now Playing: " + playing_basename, bg="#00ff00")
    btn_pause.configure(text="Pause", command=pause)

def stop():
    mixer.music.stop()
    clear_labels()
    display_playlist()
    btn_stop.configure(state="disabled")
    btn_pause.configure(text="Pause", state="disabled")
    
    lbl_playing.configure(text="", bg=bg_default, fg=fg_default)

# map the buttons to functions
btn_choose.configure(command=chooseFile)
btn_play.configure(command=play)
btn_stop.configure(command=stop)
btn_pause.configure(command=pause)

root.mainloop()