# -*- coding: utf-8 -*-
"""
    space-whiskey.library
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by the Phillip Royer.
    :license: GNU, see LICENSE for more details.
"""
import utils
import json
from game import *

class Library:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.games = []
        self.index = 0

        utils.verifyGamesDirectory()
        self.path = utils.getGamesDirectory()
        self.directories = utils.listDirectories()

    def build(self):
        for idx, directory in enumerate(self.directories):
            if utils.verifyMetadata(directory):
                with open(self.path + '/' + directory + '/metadata.json') as f:
                    data = json.load(f)
                    x = self.canvas.master.winfo_width()/2 + (idx * 250)
                    game = Game(directory, data['title'], data['description'], self.path + '/' + directory + '/' + data['image'], data['command'])
                    game.createFrame(self.canvas, x)
                    self.games.append(game)

        self.games[self.index].focus()
        self.root.bind("<Right>", self.nextGame)
        self.root.bind("<Left>", self.previousGame)

    def nextGame(self, event):
        if self.index < len(self.games) - 1:
            self.index += 1
            for game in self.games:
                game.unfocus()
                game.moveLeft()
            self.games[self.index].focus()

    def previousGame(self, event):
        if self.index > 0:
            self.index -= 1
            for game in self.games:
                game.unfocus()
                game.moveRight()
            self.games[self.index].focus()

    def getCount(self):
        return len(self.games)
