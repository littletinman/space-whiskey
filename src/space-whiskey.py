# -*- coding: utf-8 -*-
"""
    space-whiskey
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by the Phillip Royer.
    :license: BSD, see LICENSE for more details.
"""
# TODO: Mouseovers on games

import pygame
from pygame.locals import *
from utils import *
from config import *
from library import *
from message import *

config = Config()
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# Setup Controllers
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joystick in joysticks:
    joystick.init()

JOY_A_BUTTON = 1
JOY_B_BUTTON = 2
JOY_X_AXIS = 0
JOY_Y_AXIS = 1

# Setup Window
pygame.display.set_caption('Space Whiskey')
if config.fullscreen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((800, 480), 0, 32)
width, height = pygame.display.get_surface().get_size()

# Branding
# TODO: Scale with display
def drawUI():
    banner = pygame.image.load('assets/banner.png')
    banner.convert()
    screen.blit(banner, (width/2 - banner.get_size()[0]/2, 10))

    # Version, Repo, and Count
    font = pygame.font.Font('assets/space-whiskey.ttf', 9)
    version = font.render('0.1.5', False, COLOR_FG)
    screen.blit(version,(5, height - 16))
    contribute = font.render('github.com/littletinman/space-whiskey', False, COLOR_FG)
    screen.blit(contribute,(width/2 - contribute.get_size()[0]/2, height - 16))
    game_count = str(library.getCount()) + ' Games'
    count = font.render(game_count, False, COLOR_FG)
    screen.blit(count,(width - count.get_size()[0] - 5, height - 16))

# Message List
messages = []

# Build Library
library = Library(screen, messages)
library.build()

pygame.event.clear()

def update():

    global running

    if len(messages) > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                messages.pop(0)
        pass

    # Process Input
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RIGHT:
                library.nextGame()
            elif event.key == K_LEFT:
                library.previousGame()
            elif event.key == K_RETURN:
                library.launch()
        elif event.type == JOYBUTTONDOWN:
            if event.button == JOY_A_BUTTON:
                library.launch()
        elif event.type == JOYAXISMOTION:
            if event.axis == JOY_X_AXIS:
                if int(event.value) == -1:
                    library.previousGame()
                elif int(event.value) == 1:
                    library.nextGame()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for game in library.games:
                if game.rect.collidepoint(pos):
                    game.launch(messages)

def draw():
    screen.fill(COLOR_BG)
    drawUI()

    # Draw Games
    for game in library.games:
        game.update()
        if game.rect.collidepoint(pygame.mouse.get_pos()):
            game.hover()
        game.draw()

    # Draw Messages
    if len(messages) > 0:
        messages[0].draw(screen, width, height)

    pygame.display.flip()

running = True
while running:
    update()
    draw()
    clock.tick(30)

pygame.quit()
