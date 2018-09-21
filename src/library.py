# -*- coding: utf-8 -*-
"""
    space-whiskey.library
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by Phil Royer.
    :license: BSD, see LICENSE for more details.
"""
import pygame
import logging
import utils
import json
from game import *

class Library:
    def __init__(self, screen, messages):
        self.screen = screen
        self.messages = messages
        self.games = []
        self.index = 0

        utils.verifyGamesDirectory()
        self.path = utils.getGamesDirectory()
        self.directories = utils.listDirectories()

    def build(self):

        logging.info('Building library from directories')
        self.buildLibraryFromDirectories()

        logging.info('Building library from file')
        self.buildLibraryFromFile()

        if self.getCount() > 0:
            self.games[self.index].focus()

        for idx, game in enumerate(self.games):
            game.setIndex(idx)

    def buildLibraryFromDirectories(self, folder=utils.getGamesDirectory()):
        directories = utils.listDirectories(folder)
        for directory in directories:
            if utils.verifyMetadata(folder + '/' + directory):
                with open(folder + '/' + directory + '/metadata.json') as f:
                    data = json.load(f)
                    self.jsonToGame(folder + '/' + directory + '/', data)

    def buildLibraryFromFile(self):
        if utils.verifyLibraryFile():
            with open(self.path + '/library.json') as f:
                library_file = json.load(f)
                if 'games' in library_file:
                    for item in library_file['games']:
                        self.jsonToGame('External', item)
                if 'directories' in library_file:
                    for directory in library_file['directories']:
                        try:
                            self.buildLibraryFromDirectories(directory)
                        except OSError as error:
                            self.messages.append(Message('DIRECTORY ERROR', 'Unable to load Directory', error))

    def jsonToGame(self, folder,  data):
        
        try:
            if folder != 'External':
                image = folder + data['image']
            else:
                image = data['image']

            game = Game(
                folder,
                data['title'],
                data['description'],
                image,
                data['command'])
            game.create(self.screen, self.messages)
            self.games.append(game)
        except OSError as error:
            self.messages.append(Message('READ ERROR', 'Unable to read game from config file.', error))
        except KeyError as error:
            self.messages.append(Message('READ ERROR', 'Unable to read game from config file.', error))

    def nextGame(self):
        if self.index < len(self.games) - 1:
            self.index += 1
            self.setFocus(self.index)
            for game in self.games:
                game.moveLeft()

    def previousGame(self):
        if self.index > 0:
            self.index -= 1
            self.setFocus(self.index)
            for game in self.games:
                game.moveRight()

    def setFocus(self, index):
        self.index = int(index)
        for game in self.games:
            game.unfocus()
        self.games[self.index].focus()
        pygame.display.flip()

    def launch(self):
        self.games[self.index].launch(self.messages)

    def getCount(self):
        return len(self.games)
