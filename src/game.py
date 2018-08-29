# -*- coding: utf-8 -*-
"""
    space-whiskey.game
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by the Phillip Royer.
    :license: BSD, see LICENSE for more details.
"""
import pygame
import subprocess
import utils
import textwrap

class Game:
    def __init__(self, directory, title, description, image, command):
        self.directory = directory
        self.title = title
        self.description = description
        self.image = image
        self.command = command
        self.focused = False
        self.x = 0
        self.y = 0
        self.width = 220
        self.height = 220
        self.rect = pygame.Rect(self.x - 7, self.y -7, self.width, self.height) 

    def create(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 12)

        if self.image != None:
            self.image = pygame.image.load(self.image)
            self.image.convert()
        else:
            self.image = self.font.render('NO IMAGE', False, (255, 255, 255))

        self.label = self.font.render(self.title, False, (255, 255, 255))
        self.label_desc = self.font.render(self.description, False, (255, 255, 255))

    def launch(self, event):
        # TODO: Check if game is already running
        subprocess.Popen(self.command + " " + utils.getGamesDirectory() + '/' + self.directory + "/")

    def focus(self):
        if not self.focused:
            self.focused = True
            self.x = self.screen.get_size()[0]/2 - self.width/2
            self.y = self.screen.get_size()[1]/3
            self.rect = pygame.Rect(self.x - 7, self.y -7, self.width, self.height) 

    def unfocus(self):
        self.focused = False
        self.x, self.y = self.screen.get_size()

    def unfocusRight(self):
        self.x = self.screen.get_size()[0]/3 * 2
        self.y = self.screen.get_size()[1]/3
        self.rect = pygame.Rect(self.x - 7, self.y -7, self.width, self.height) 

    def unfocusLeft(self):
        self.x = self.screen.get_size()[0]/3 - self.width
        self.y = self.screen.get_size()[1]/3
        self.rect = pygame.Rect(self.x - 7, self.y -7, self.width, self.height) 

    def draw(self, over=False):
        if over or self.focused:
            pygame.draw.rect(self.screen, (255,255,255), self.rect, 2)
        else:
            pygame.draw.rect(self.screen, (0,0,0), self.rect, 2)

        pygame.draw.rect(self.screen, (255,255,255), (self.x - 7, self.y -7, self.width, self.height), 2)
        self.screen.blit(self.image, (self.x + self.width/2 - self.image.get_size()[0]/2, self.y))
        self.screen.blit(self.label, (self.x, self.y + 130))
        if self.focused:
            self.screen.blit(self.label_desc, (self.x, self.y + 150))
 

