# -*- coding: utf-8 -*-
"""
    space-whiskey
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by the Phillip Royer.
    :license: BSD, see LICENSE for more details.
"""

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
from config import *
from library import *

config = Config()
root = tk.Tk()

# Setup Window
root.title('Space Whiskey')
if config.fullscreen:
    root.attributes("-fullscreen", True)
    root.wm_attributes("-topmost", 1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.focus_set()
else:
    root.geometry("800x480")
    root.resizable(0, 0)
    root.focus_set()

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
version = canvas.create_text(10, canvas.winfo_height() - 5, anchor=SW, fill="white", text="0.0.3")
contribute = canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height() - 5, anchor=S, fill="white", text="github.com/littletinman/space-whiskey")
count = canvas.create_text(canvas.winfo_width() - 5, canvas.winfo_height() - 5, anchor=SE, fill="white", text="0 Games")

# Build Library
library = Library(root, canvas)
library.build()

# Games
updated_count = str(library.getCount()) + " Games"
canvas.itemconfigure(count, text=updated_count)

def _quit(event):
    root.destroy()

root.bind("<Escape>", _quit)

## Uncomment for autoclose
# root.after(5000, root.destroy) 

# Run
root.mainloop()
