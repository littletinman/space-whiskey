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
import subprocess
import json
games = []

# TODO: Turn into class and take care of folders here

def buildLibrary(canvas, directories, path):
    for idx, directory in enumerate(directories):
        if utils.verifyMetadata(directory):
            with open(path + '/' + directory + '/metadata.json') as f:
                data = json.load(f)

                game = {}
                game['directory'] = directory
                game['title'] = data['title']
                game['description'] = data['description']
                game['image'] = path + '/' + directory + '/' + data['image']
                game['command'] = data['command']

                image = PhotoImage(file=game['image'])
                if idx == 0:
                    scaled_image = image.zoom(1, 1)
                else:
                    scaled_image = image.zoom(1, 1)

                x = idx * (scaled_image.width() + 50)
                game['canvas'] = Canvas(master=canvas, width=200, height=200, bg='black', highlightthickness=0)

                # TODO: Figure out why only last image shows up
                game['promo'] = game['canvas'].create_image(0, 0, anchor=NW, image=scaled_image)
                game['label'] = game['canvas'].create_text(0, 135, anchor=NW, font=('TkDefaultFont', 10), fill="white", text=game['title'])
                game['desc'] = game['canvas'].create_text(0, 155, anchor=NW, fill="white", text=game['description'])
                game['canvas'].pack()
                game['window'] = canvas.create_window(canvas.winfo_width()/2 + x, canvas.winfo_height()/2 + 20, anchor=CENTER, window=game['canvas'])

                games.append(game)

def startGame():
    print(games[0]['command'] + " " + utils.getGamesDirectory() + '/' + games[0]['directory'] + "/")
    p = subprocess.Popen(games[0]['command'] + " " + utils.getGamesDirectory() + '/' + games[0]['directory'] + "/")
