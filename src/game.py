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
        self.focused = False

    def createFrame(self, master, x):
        self.image = PhotoImage(file=self.image)
        self.frame = tk.Frame(master=master, width=220, height=220, pady=10, padx=10, bg='black', highlightthickness=2, highlightbackground='black', cursor="hand2")
        self.promo = tk.Label(self.frame, anchor=N, image=self.image, bg='black', borderwidth=0, relief="groove")
        self.label = tk.Label(self.frame, anchor=W, justify=LEFT, pady=5, bg='black', fg='white', wraplength=200, borderwidth=0, text=self.title + "\n\n" + self.description + "test test test test test test test test test")

        self.master = master

        self.promo.pack(fill='x')
        self.label.pack(fill='x')

        self.frame.bind('<Button-1>', self.launch)
        self.label.bind('<Button-1>', self.launch)
        self.promo.bind('<Button-1>', self.launch)
        self.frame.bind('<Enter>', self.enter)
        self.frame.bind('<Leave>', self.leave)

        self.frame.pack_propagate(0)
        master.create_window(x, master.winfo_height()/2 + 20, anchor=CENTER, window=self.frame)

    def launch(self, event):
        # TODO: Check if game is already running
        subprocess.Popen(self.command + " " + utils.getGamesDirectory() + '/' + self.directory + "/")

    def enter(self, event):
        if self.focused:
            self.frame.config(width=240, height=240, pady=20, padx=20, highlightthickness=2, highlightbackground='white')
        else:
            self.frame.config(highlightthickness=2, highlightbackground='white')

    def leave(self, event):
        if self.focused:
            self.frame.config(width=240, height=240, pady=20, padx=20, highlightthickness=1, highlightbackground='white')
        else:
            self.frame.config(highlightthickness=2, highlightbackground='black')

    def focus(self):
        self.focused = True
        self.frame.config(width=240, height=240, pady=20, padx=20, highlightthickness=1, highlightbackground='white')

    def unfocus(self):
        self.focused = False
        self.frame.config(width=220, height=220, pady=10, padx=10, highlightthickness=2, highlightbackground='black')

    def moveLeft(self):
        self.frame.place(x=self.frame.winfo_x() - 250, y=self.frame.winfo_y())

    def moveRight(self):
        self.frame.place(x=self.frame.winfo_x() + 250, y=self.frame.winfo_y())
