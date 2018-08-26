# -*- coding: utf-8 -*-
"""
    space-whiskey
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by the Phillip Royer.
    :license: BSD, see LICENSE for more details.
"""
import pygame
from pygame.locals import *
from config import *
from library import *

config = Config()
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# Setup Window
pygame.display.set_caption("Space Whiskey")
if config.fullscreen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((800, 480), 0, 32)
width, height = pygame.display.get_surface().get_size()
screen.fill((0,0,0))

# Branding
# TODO: Scale with display
def drawUI():
    banner = pygame.image.load('assets/banner.png')
    banner.convert()
    screen.blit(banner, (width/2 - banner.get_size()[0]/2, 10))

    # Version, Repo, and Count
    font = pygame.font.SysFont('Arial', 12)
    version = font.render('0.1.0', False, (255, 255, 255))
    screen.blit(version,(5, height - 16))
    contribute = font.render('github.com/littletinman/space-whiskey', False, (255, 255, 255))
    screen.blit(contribute,(width/2 - contribute.get_size()[0]/2, height - 16))
    game_count = str(library.getCount()) + " Games"
    count = font.render(game_count, False, (255, 255, 255))
    screen.blit(count,(width - count.get_size()[0] - 5, height - 16))

# Build Library
library = Library(screen)
library.build()

pygame.event.clear()

running = True
while running:

    drawUI()
    pygame.display.flip()

    event = pygame.event.wait()
    if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
        running = False
    elif event.type == KEYDOWN and event.key == K_RIGHT:
        library.nextGame()
    elif event.type == KEYDOWN and event.key == K_LEFT:
        library.previousGame()

pygame.quit()
