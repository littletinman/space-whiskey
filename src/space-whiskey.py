try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    from Tkinter import *
import os
import subprocess
import json
import utils
import library

# Setup
root = tk.Tk()

# Window Mode
root.title('Space Whiskey')
root.geometry("800x480")
root.resizable(0, 0)

# Fullscreen
#root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.focus_set()

# Main Canvas
canvas = Canvas(master=root, bg='black', highlightthickness=0)
canvas.pack_propagate(0)
canvas.pack(fill=tk.BOTH, expand=1)
root.update()

# Branding
origBrandingImage = PhotoImage(file="assets/banner.png")
# TODO: Calculate Zoom Percentage
brandingImage = origBrandingImage.zoom(1, 1)
branding = canvas.create_image(canvas.winfo_width()/2, 15, anchor=N, image=brandingImage)

# Version and Repo
version = canvas.create_text(10, canvas.winfo_height() - 5, anchor=SW, fill="white", text="0.0.1")
contribute = canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height() - 5, anchor=S, fill="white", text="github.com/littletinman/space-whiskey")
count = canvas.create_text(canvas.winfo_width() - 5, canvas.winfo_height() - 5, anchor=SE, fill="white", text="0 Games")

# User Path
path = os.path.expanduser("~/")
utils.verifyGamesDirectory()

# Games
directories = utils.listDirectories()
updated_count = str(len(directories)) + " Games"
canvas.itemconfigure(count, text=updated_count)

# Build Library
library.buildLibrary(canvas, directories, utils.getGamesDirectory())

def runGame(e):
    library.startGame()

root.bind("<space>", runGame)

def _quit(event):
    root.destroy()

root.bind("<Escape>", _quit)

# Run
root.mainloop()
