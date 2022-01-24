import sys
from tkinter import *
import os.path

# gets file included with pyinstaller
def get_path(filepath):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filepath)
    else:
        return filepath

# window declaration
root = Tk()
root.geometry("700x350")
root.title("Audio Player")

#Make the window sticky for every case
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# set window icon
root.iconbitmap(get_path("icon.ico"))

# widget declaration
lbl_title = Label(root, text="MP3 Player", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), bg="white", fg="Gray")

frame1 = LabelFrame(root)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(2, weight=1)
btn_choose = Button(frame1, text="Choose File")
lbl_playing = Label(frame1)
lbl_queue = Label(frame1)

frame_buttons = LabelFrame(root, padx=5, pady=5)
frame_buttons.grid_rowconfigure(0, weight=1)
frame_buttons.grid_columnconfigure(2, weight=1)
btn_play = Button(frame_buttons, text="Play queued", state="disabled", width=10)
btn_stop = Button(frame_buttons, text="Stop", state="disabled", width=10)
btn_pause = Button(frame_buttons, text="Pause", state="disabled", width=10)

# widget packing
colspan_lbl = 6
colspan_btn = 2
lbl_title.grid(row=0, columnspan=colspan_lbl)

frame1.grid(row=1, column=0, columnspan=colspan_lbl, sticky=W+E, padx=10)
btn_choose.grid(row=1, column=2, columnspan=colspan_btn)
lbl_playing.grid(row=2, column=0, columnspan=colspan_lbl)
lbl_queue.grid(row=3, column=0, columnspan=colspan_lbl)

frame_buttons.grid(row=2, columnspan=colspan_lbl, sticky=W+E, padx=10, pady=10)
btn_play.grid(row=0, column=0, rowspan=2, columnspan=colspan_btn)
btn_pause.grid(row=0, column=2, rowspan=2, columnspan=colspan_btn)
btn_stop.grid(row=0, column=4, rowspan=2, columnspan=colspan_btn)

# get default widget colors
bg_default = lbl_queue.cget("bg")
fg_default = lbl_queue.cget("fg")