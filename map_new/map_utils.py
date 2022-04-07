import pygame as pg
from map_new.tile import Tile

MAP_WIDTH = 5
MAP_HEIGHT = 5

TILE_SIZE_PX = 64

# tworzenie pustego arraya o podanych wymiarach
def getBlankMapArray():
    map = [[0 for x in range(0,MAP_WIDTH)] for y in range (0,MAP_HEIGHT)]

    map[0][1] = 1
    map[0][2] = 1

    return map

# tworzenie surface poprzed czytanie arraya i wedle niego wypelnianie konkretnymi tile'ami
# def makeSurfaceMap(map, pattern):
#     surface = pg.Surface((MAP_WIDTH * TILE_SIZE_PX, MAP_HEIGHT * TILE_SIZE_PX))

#     for i in range(len(map)):
#         offsetY = i * TILE_SIZE_PX
#         for j in range(len(map[i])):
#             offsetX = j * TILE_SIZE_PX
#             surface.blit(pattern[map[i][j]], (offsetX, offsetY))
#     return surface

# tworzenie grup sprite'ow
def getSprites(map, pattern):
    roadTiles = pg.sprite.Group()
    wallTiles = pg.sprite.Group()

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







