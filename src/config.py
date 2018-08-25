# -*- coding: utf-8 -*-
"""
    space-whiskey.config
    ~~~~~~~~~~~~~~
    :copyright: © 2018 by the Phillip Royer.
    :license: BSD, see LICENSE for more details.
"""
import os
import utils
import json
import logging

class Config:
    def __init__(self):
        self.file = "config.json"
        self.fullscreen = True
        self.logfile = "error.log"

        if self.hasConfig():
            self.readConfig()
            self.setupLogging()

    def hasConfig(self):
        return os.path.isfile(self.file)

    def readConfig(self):
        with open('config.json') as f:
            data = json.load(f)
            self.fullscreen = data['fullscreen']
            self.logfile = data['logfile']

    def setupLogging(self):
        # clear log file evrytime the application opens
        with open(self.logfile, 'w'):
            pass
        logging.basicConfig(filename=self.logfile, level=logging.DEBUG)
