# -*- coding: utf-8 -*-
"""
    space-whiskey.game
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

    def createFrame(self, master):
        self.frame = tk.Frame(
                master=master,
                width=220, height=220,
                pady=10, padx=10,
                bg='black', cursor="hand2",
                highlightthickness=2, highlightbackground='black')
        if self.image != None:
            self.image = PhotoImage(file=self.image)
            self.promo = tk.Label(self.frame, anchor=N, image=self.image, bg='black', borderwidth=0)
        else:
            self.promo = tk.Label(self.frame, anchor=N, pady=50, text="NO IMAGE")
        self.label = tk.Label(
                self.frame, anchor=W, justify=LEFT,
                pady=10, bg='black', fg='white',
                wraplength=200, borderwidth=0,
                text=self.title + "\n\n" + self.description)

        self.master = master

        self.promo.pack(fill='x')
        self.label.pack(fill='x')

        self.frame.bind('<Button-1>', self.launch)
        self.label.bind('<Button-1>', self.launch)
        self.promo.bind('<Button-1>', self.launch)
        self.frame.bind('<Enter>', self.enter)
        self.frame.bind('<Leave>', self.leave)

        self.frame.pack_propagate(0)
        master.create_window(master.winfo_width() - 1, master.winfo_height() - 1, anchor=NW, window=self.frame)

    def launch(self, event):
        # TODO: Check if game is already running
        subprocess.Popen(self.command + " " + utils.getGamesDirectory() + '/' + self.directory + "/")

    def enter(self, event):
        if self.focused:
            self.frame.config(highlightthickness=2, highlightbackground='white')
        else:
            self.frame.config(highlightthickness=2, highlightbackground='white')

    def leave(self, event):
        if self.focused:
            self.frame.config(highlightthickness=2, highlightbackground='white')
        else:
            self.frame.config(highlightthickness=2, highlightbackground='black')

    def focus(self):
        if not self.focused:
            self.focused = True
            self.frame.update()
            self.frame.config(highlightthickness=2, highlightbackground='white')
            self.frame.place(x=self.master.winfo_width()/2, anchor=CENTER, y=self.master.winfo_height()/2 + 20)

    def unfocus(self):
        self.focused = False
        self.frame.update()
        self.frame.config(highlightthickness=2, highlightbackground='black')
        self.frame.place(anchor=NW, x=self.master.winfo_width() - 1, y=self.master.winfo_height() - 1)

    def unfocusRight(self):
        self.frame.update()
        self.frame.config(highlightthickness=2, highlightbackground='black')
        self.frame.place(x=self.master.winfo_width()/2 + 250, anchor=CENTER, y=self.master.winfo_height()/2 + 20)

    def unfocusLeft(self):
        self.frame.update()
        self.frame.config(highlightthickness=2, highlightbackground='black')
        self.frame.place(x=self.master.winfo_width()/2 - 250, anchor=CENTER, y=self.master.winfo_height()/2 + 20)
