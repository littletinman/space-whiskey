# -*- coding: utf-8 -*-
"""
    space-whiskey.game
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by Phil Royer.
    :license: BSD, see LICENSE for more details.
"""
import traceback
import pygame
import subprocess
import utils
import textwrap
from message import *

class Game:
    def __init__(self, directory, title, description, image, command):
        self.directory = directory
        self.title = title
        self.description = description
        self.image = image
        self.command = command
        self.focused = False
        self.over = False
        self.arrived = True
        self.index = 0
        self.x = 0
        self.targetX = 0
        self.y = 0
        self.pad = 6
        self.width = 210
        self.height = 210
        self.rect = pygame.Rect(self.x - self.pad, self.y -self.pad, self.width, self.height)

    def create(self, screen, messages):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 12)

        if self.image != None:
            try:
                self.image = pygame.image.load(self.image)
                self.image.convert()
                self.image = pygame.transform.scale(self.image, (200, 120))
            except pygame.error as error:
                self.image = self.font.render('NO IMAGE', False, (255, 255, 255))
                messages.append(Message("IMAGE ERROR", "Unable to find image for " + self.title + ".", error))
        else:
            self.image = self.font.render('NO IMAGE', False, (255, 255, 255))

        self.label = self.font.render(self.title, False, (255, 255, 255))
        self.label_desc = self.font.render(self.description, False, (255, 255, 255))

    def setIndex(self, index):
        self.index = index
        self.x = self.screen.get_size()[0]/2 - self.width/2 + self.pad + (270 * index)
        self.targetX = self.x
        self.y = self.screen.get_size()[1]/3

    def launch(self, messages):
        
        if self.command == None:
            messages.append(Message("LAUNCH ERROR", "No Command For '" + self.title + "'", None))
            return

        try:
            if self.directory == 'External':
                p = subprocess.Popen(self.command)
            else:
                p = subprocess.Popen(self.command, cwd=self.directory + '/')
            p.wait()
        except OSError as error:
            messages.append(Message("LAUNCH ERROR", "Unable to launch game", error))

    def focus(self):
        if not self.focused:
            self.focused = True

    def unfocus(self):
        self.focused = False

    def hover(self):
        self.over = True

    def update(self):
        self.over = False
        if self.x != self.targetX:
            self.arrived = False
            if self.x > self.targetX:
                self.x -= 270/5
            elif self.x < self.targetX:
                self.x += 270/5
        else:
            self.arrived = True

    def moveRight(self):
        self.targetX += 270

    def moveLeft(self):
        self.targetX -= 270

    def draw(self):
        self.rect = pygame.Rect(self.x - self.pad, self.y -self.pad, self.width, self.height)
        if self.over or self.focused and self.arrived:
            pygame.draw.rect(self.screen, (255,255,255), self.rect, 2)
        else:
            pygame.draw.rect(self.screen, (0,0,0), self.rect, 2)
        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.label, (self.x, self.y + 130))
        if self.focused:
            self.screen.blit(self.label_desc, (self.x, self.y + 150))
