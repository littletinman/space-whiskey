# -*- coding: utf-8 -*-
"""
    space-whiskey.utils
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by the Phillip Royer.
    :license: BSD, see LICENSE for more details.
"""
import os

user_path = os.path.expanduser("~/")
games_path = user_path + "Games"

def verifyGamesDirectory():
    if not folderExists():
        createFolder()

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
    return os.path.isfile(directory + "/metadata.json")

def libraryFileExists():
    return os.path.isfile(games_path + "/library.json")

def createFolder():
    os.makedirs(games_path)

def validateMetadata():

    return

def listDirectories(folder=games_path):
    return [ name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name)) ]
