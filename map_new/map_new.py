from map_new import map_utils
from map_new import map_pattern
import pygame as pg
from settings import *

# def getMap():
#     array = map_utils.getBlankMapArray()
#     pattern = map_pattern.getPattern()
#     surface = map_utils.makeSurfaceMap(array, pattern)
#     return surface

def getTiles():
    array = map_utils.getBlankMapArray()
    pattern = map_pattern.getPattern()
    tiles = map_utils.getSprites(array, pattern)
    return tiles

def renderTiles(tiles, screen, camera, debug=False):
    for tile in tiles:
        screen.blit(tile.image, camera.apply_rect(tile.rect))
        if debug:
            pg.draw.rect(screen, RED, camera.apply_rect(tile.rect), 1)
