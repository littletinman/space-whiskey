# -*- coding: utf-8 -*-
"""
    space-whiskey.library
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by the Phillip Royer.
    :license: BSD, see LICENSE for more details.
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
                    game = Game(
                            directory,
                            data['title'],
                            data['description'],
                            self.path + '/' + directory + '/' + data['image'],
                            data['command'])
                    game.createFrame(self.canvas)
                    self.games.append(game)

        self.buildLibraryFromFile()

        if self.getCount() > 0:
            self.games[self.index].focus()
            if (self.index + 1) <= (self.getCount() - 1):
                self.games[self.index + 1].unfocusRight()
            self.root.bind("<Right>", self.nextGame)
            self.root.bind("<Left>", self.previousGame)

    def buildLibraryFromFile(self):
        if utils.verifyLibraryFile():
            with open(self.path + '/library.json') as f:
                library_file = json.load(f)
                for item in library_file['games']:
                    game = Game(
                            'Games',
                            item['title'],
                            item['description'],
                            item['image'],
                            item['command'])
                    game.createFrame(self.canvas)
                    self.games.append(game)


    def nextGame(self, event):
        if self.index < len(self.games) - 1:
            self.index += 1
            for game in self.games:
                game.unfocus()
            if self.index > 0:
                self.games[self.index - 1].unfocusLeft()
            self.games[self.index].focus()
            if self.index < self.getCount() - 1:
                self.games[self.index + 1].unfocusRight()

    def previousGame(self, event):
        if self.index > 0:
            self.index -= 1
            for game in self.games:
                game.unfocus()
            if self.index > 0:
                self.games[self.index - 1].unfocusLeft()
            self.games[self.index].focus()
            if self.index < self.getCount() - 1:
                self.games[self.index + 1].unfocusRight()

    def getCount(self):
        return len(self.games)
