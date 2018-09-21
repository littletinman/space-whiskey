# -*- coding: utf-8 -*-
"""
    space-whiskey.utils
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by Phil Royer.
    :license: BSD, see LICENSE for more details.
"""
import os, json

COLOR_BG = (0,0,0)
COLOR_FG = (255,255,255)

user_path = os.path.expanduser('~/')
games_path = user_path + 'Games'

def verifyGamesDirectory():
    if not folderExists():
        createFolder()
        createJSON()
    else:
        if not libraryFileExists():
            createJSON()

def verifyLibraryFile():
    if libraryFileExists():
        # TODO validate fields
        return True
    else:
        return False

def verifyMetadata(directory):
    if metadataExists(directory):
        # TODO validate fields
        return True
    else:
        return False

def getGamesDirectory():
    return games_path

# Helper Functions

def folderExists():
    return os.path.exists(games_path)

def metadataExists(directory):
    return os.path.isfile(directory + '/metadata.json')

def libraryFileExists():
    return os.path.isfile(games_path + '/library.json')

def createFolder():
    os.makedirs(games_path)

def createJSON():
    json_file = open(games_path + '/library.json','w+')
    json.dump({'games': [], 'directories': []}, json_file, indent=4)

def validateMetadata():

    return

def listDirectories(folder=games_path):
    return [ name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name)) ]
