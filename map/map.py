from map import map_utils
from map import map_pattern
import pygame as pg
from settings import *

def get_tiles():
    # array = map_utils.generate_map()
    array = map_utils.get_blank_map_array()

    array[1][1] = 1
    array[1][2] = 1
    array[1][3] = 1
    array[1][4] = 1
    array[1][5] = 1
    array[1][6] = 1

    array[2][5] = 1

    pattern = map_pattern.get_pattern()
    tiles = map_utils.get_sprites(array, pattern)
    return tiles, array

def render_tiles(tiles, screen, camera, debug=False):
    for tile in tiles:
        screen.blit(tile.image, camera.apply_rect(tile.rect))
        if debug:
            pg.draw.rect(screen, RED, camera.apply_rect(tile.rect), 1)
