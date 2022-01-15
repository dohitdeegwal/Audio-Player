from tkinter import Tk, Label, Button, TOP, X, GROOVE
from tkinter.filedialog import askopenfilename
import os.path

filepath = ""
valid = False
default_bg =""
valid_extensions = (".mp3", ".wav", ".ogg")

#gets the filepath and checks for valid extension
def chooseFile():
    filename_lbl.config(text="Choosing file...", bg = default_bg)
    validity_lbl.config(text="", bg = default_bg)
    
    filepath = askopenfilename()
    filename_lbl.config(text=os.path.basename(filepath))

    if(not os.path.exists(filepath)):
        filename_lbl.config(text="Invalid Path!" + filepath, bg="red")
    else:
        extension = os.path.splitext(filepath)[1]
        if extension not in valid_extensions:
            filename_lbl.config(bg="red")
            validity_lbl.config(text="Unsupported File extension: " + extension +"\nChoose from: " + ", ".join(valid_extensions))
        else:
            filename_lbl.config(bg="green")
            valid = True

window = Tk()
window.title("Audio Player")
window.geometry("500x400")

#widget declaration
title=Label(window, text="MP3 Player", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), bg="white", fg="Gray")
choose_btn = Button(master=window, text="Choose File", command=chooseFile)
filename_lbl = Label(window)
validity_lbl = Label(window)

#widget packing
title.pack(side=TOP, fill=X)
choose_btn.pack(pady=10)
filename_lbl.pack()
validity_lbl.pack(pady=5)

#get default widget bg color
default_bg = validity_lbl.cget('bg')

window.mainloop()
