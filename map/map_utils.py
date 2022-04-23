import random
import pygame as pg
from settings import *
from map.tile import Tile

# tworzenie pustego arraya o podanych wymiarach
def get_blank_map_array():
    map = [[0 for x in range(0,MAP_WIDTH)] for y in range (0,MAP_HEIGHT)]
    return map

# generowanie obiektow na mapie
def generate_map():
    map = get_blank_map_array()
    for i in range(0, 20):
        x = random.randint(0, MAP_WIDTH-1)
        y = random.randint(0, MAP_HEIGHT-1)
        map[y][x] = 1
    return map

# tworzenie grup sprite'ow
def get_sprites(map, pattern):
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

class Camera:
    def __init__(self,width,height):
        self.camera = pg.Rect(0,0, width, height)
        self.width = width
        self.height = height

    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
         return rect.move(self.camera.topleft)
    
    def update(self,target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)








