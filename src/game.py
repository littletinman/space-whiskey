# -*- coding: utf-8 -*-
"""
    space-whiskey.game
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by the Phillip Royer.
    :license: GNU, see LICENSE for more details.
"""
try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    from Tkinter import *
import subprocess
import utils

class Game:
    def __init__(self, directory, title, description, image, command):
        self.directory = directory
        self.title = title
        self.description = description
        self.image = image
        self.command = command

    def createFrame(self, master, x):
        self.image = PhotoImage(file=self.image)
        self.frame = tk.Frame(master=master, width=210, height=210, pady=5, padx=5, bg='black')
        self.promo = tk.Label(self.frame, anchor=N, image=self.image, bg='black', borderwidth=0)
        self.label = tk.Label(self.frame, anchor=W, justify=LEFT, pady=5, bg='black', fg='white', wraplength=200, borderwidth=0, text=self.title + "\n\n" + self.description + "test test test test test test test test test")
        self.promo.pack(fill='x')
        self.label.pack(fill='x')
        self.promo.bind('<Button-1>', self.launch)
        self.label.bind('<Button-1>', self.launch)
        self.frame.pack_propagate(0)
        master.create_window(x, master.winfo_height()/2 + 20, anchor=CENTER, window=self.frame)

    def launch(self, event):
        subprocess.Popen(self.command + " " + utils.getGamesDirectory() + '/' + self.directory + "/")
