# -*- coding: utf-8 -*-
"""
    space-whiskey.game
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by Phil Royer.
    :license: BSD, see LICENSE for more details.
"""
import pygame
import subprocess
from utils import *
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
        self.ease = 0.45
        self.y = 0
        self.pad = 3
        self.width = 200
        self.height = 200
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.inverted = False
        self.desc_color = COLOR_FG

    def create(self, screen, messages):
        self.screen = screen
        self.font = pygame.font.Font('assets/space-whiskey.ttf', 9)

        if self.image != None:
            try:
                self.image = pygame.image.load(self.image)
                self.image.convert()
                self.image = pygame.transform.scale(self.image, (200, 120))
            except pygame.error as error:
                self.image = pygame.image.load('assets/no-image.png') 
                self.image.convert()
                self.image = pygame.transform.scale(self.image, (200, 120))
                messages.append(Message('IMAGE ERROR', 'Unable to find image for ' + self.title + '.', error))
        else:
            self.image = pygame.image.load('assets/no-image.png') 
            self.image.convert()
            self.image = pygame.transform.scale(self.image, (200, 120))

        self.label = self.font.render(self.title, False, COLOR_FG)
        self.desc_lines = self.wrapDesc(self.description, self.font)
    
    def wrapDesc(self, description, font):
        lines = []
        self.desc_split = description.split(' ')
        self.curr_width = font.size(description)[0]
        self.new_line = ''
        while self.curr_width > self.width - self.pad:
            # cut off words one by one, put them into another line
            self.new_line = self.desc_split[-1] + ' ' + self.new_line
            self.desc_split.pop()
            self.curr_width = font.size(' '.join(self.desc_split))[0]
        lines.append(self.font.render(' '.join(self.desc_split), False, self.desc_color))
        if(font.size(self.new_line)[0] > self.width):
            #recursively make more lines
            lines.extend(self.wrapDesc(self.new_line, font))
        else:
            lines.append(self.font.render(self.new_line, False, self.desc_color))
        return lines
        
            
    def setIndex(self, index):
        self.index = index
        self.x = self.screen.get_size()[0]/2 - self.width/2 + (270 * index)
        self.targetX = self.x
        self.y = self.screen.get_size()[1]/3

    def launch(self, messages):
        
        if self.command == None:
            messages.append(Message('LAUNCH ERROR', 'No Command For "' + self.title + '"', None))
            return

        try:
            if self.directory == 'External':
                p = subprocess.Popen(self.command)
            else:
                p = subprocess.Popen(self.command, cwd=self.directory + '/')
            p.wait()
        except OSError as error:
            messages.append(Message('LAUNCH ERROR', 'Unable to launch game', error))

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
            dx = float(self.targetX - self.x)
            vx = dx * self.ease
            self.x += vx
            self.x = int(round(self.x))
            if abs(dx) < 3:
                self.x = self.targetX
        else:
            self.arrived = True

    def moveRight(self):
        self.targetX += 270

    def moveLeft(self):
        self.targetX -= 270

    def invert(self):
        if not self.inverted:
            self.inverted = True
            self.label = self.font.render(self.title, False, COLOR_BG)
            self.desc_color = COLOR_BG
            self.desc_lines = self.wrapDesc(self.description, self.font)

    def uninvert(self):
        if self.inverted:
            self.inverted = False
            self.label = self.font.render(self.title, False, COLOR_FG)
            self.desc_color = COLOR_FG
            self.desc_lines = self.wrapDesc(self.description, self.font)
    
    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.over or self.focused and self.arrived:
            pygame.draw.rect(self.screen, COLOR_FG, self.rect)
            self.invert()
        else:
            pygame.draw.rect(self.screen, COLOR_BG, self.rect)
            self.uninvert()
        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.label, (self.x + self.pad, self.y + 120 + (2 * self.pad)))
        if self.focused:
            for line in range(len(self.desc_lines)):
                #blit all the lines we made in wrapDesc, checking if the next line would not fit
                if 12 * (line + 1) < 48: 
                    self.screen.blit(self.desc_lines[line], (self.x + self.pad, self.y + 146 + 12 * line))
                else:
                    self.screen.blit(pygame.font.Font('assets/space-whiskey.ttf', 9).render('...', False, self.desc_color), 
                                     (self.x + self.pad, self.y + 146 + 12 * line))
                    break
