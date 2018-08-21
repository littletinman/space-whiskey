# -*- coding: utf-8 -*-
"""
    space-whiskey.library
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
import utils
import json
from game import *
games = []

# TODO: Turn into class and take care of folders here

def buildLibrary(canvas, directories, path):
    for idx, directory in enumerate(directories):
        if utils.verifyMetadata(directory):
            with open(path + '/' + directory + '/metadata.json') as f:
                data = json.load(f)
                x = canvas.master.winfo_width()/2 + (idx * 250)
                print(x)
                game = Game(directory, data['title'], data['description'], path + '/' + directory + '/' + data['image'], data['command'])
                game.createFrame(canvas, x)
                games.append(game)
