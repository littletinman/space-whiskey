# -*- coding: utf-8 -*-
"""
    space-whiskey.message
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by Phil Royer.
    :license: BSD, see LICENSE for more details.
"""
import pygame 
from utils import *

class Message:
    def __init__(self, title, content, error):
        self.fontSmall = pygame.font.Font('assets/space-whiskey.ttf', 12)
        self.fontLarge = pygame.font.Font('assets/space-whiskey.ttf', 27)
        self.title   = self.fontLarge.render(title, False, COLOR_FG)
        self.content = self.fontSmall.render(content, False, COLOR_FG)
        if error == None: error = ''
        self.error   = self.fontSmall.render(str(error), False, COLOR_FG)
        self.dismiss = self.fontSmall.render('Press any key to dismiss this message', False, COLOR_FG)

    def draw(self, screen, width, height):
        self.rect = pygame.Rect(50, 50, width - 100, height - 100)
        pygame.draw.rect(screen, COLOR_BG, self.rect)
        pygame.draw.rect(screen, COLOR_FG, self.rect, 2)
        screen.blit(self.title, (width/2 - self.title.get_size()[0]/2, 60))
        screen.blit(self.content, (width/2 - self.content.get_size()[0]/2, height/2 - 50))
        screen.blit(self.error, (width/2 - self.error.get_size()[0]/2, height/2 - 10))
        screen.blit(self.dismiss, (width/2 - self.dismiss.get_size()[0]/2, height - 80))
