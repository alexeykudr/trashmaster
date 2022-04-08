import random
import pygame as pg
from settings import *
from map_new.tile import Tile

# tworzenie pustego arraya o podanych wymiarach
def getBlankMapArray():
    map = [[0 for x in range(0,MAP_WIDTH)] for y in range (0,MAP_HEIGHT)]
    return map

# generowanie obiektow na mapie
def generateMap():
    map = getBlankMapArray()
    for i in range(0, 20):
        x = random.randint(0, MAP_WIDTH-1)
        y = random.randint(0, MAP_HEIGHT-1)
        map[y][x] = 1
    return map

# tworzenie grup sprite'ow
def getSprites(map, pattern):
    roadTiles = pg.sprite.Group()
    wallTiles = pg.sprite.Group()

    #objechanie tablicy i generowanie tile'a na danych kordach
    for i in range(len(map)):
        offsetY = i * TILE_SIZE_PX
        for j in range(len(map[i])):
            offsetX = j * TILE_SIZE_PX
            tileId = map[i][j]
            tile = Tile(pattern[tileId], offsetX, offsetY, TILE_SIZE_PX, TILE_SIZE_PX)
            if tileId == 0:
                roadTiles.add(tile)
            else:
                wallTiles.add(tile)

    return roadTiles, wallTiles








