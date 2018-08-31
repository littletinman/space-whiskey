# Space Whiskey
An Open Game Launcher

## What is Space Whiskey
Space Whiskey is a game launcher for the Raspberry Pi and other systems.
It is designed to allow you to browse your games easily with only the addition of a simple config file.

## How it Works
- Looks in the Games folder of the current user
- Looks in each folder for a metadata.json file
- Looks in the Games folder for a library.json file for external games
- Lists the games in a minimal user interface
- Provides a simple way to launch any of the games

## Sample config.json
This file goes in the src folder of Space Whiskey but is not required:
```
{
    "fullscreen": false,
    "logfile": log.log
}
```

## Sample metadata.json
This file should be included in your game directory:
```
{
  "title": "My Game",
  "description": "A great game",
  "image": "200x120-image-for-game.png*",
  "command": "start command for game"
}
```

## Sample library.json
This file should go in the /Games directory of your user
```
{
  "games": [
    {
      "title": "My Game 1",
      "description": "A great game",
      "image": null or absolute path*,
      "command": "game executable"
    }
  ],
  "directories": ["absolute/path/to/game/directory"]
}
```

## Install
1. clone repo
2. install python and pygame
3. Setup config files accordingly
4. run ```python space-whiskey.py```
