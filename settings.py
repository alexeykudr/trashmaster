import pygame as pg

vec = pg.math.Vector2

#colors
LIGHTGREY = (100, 100, 100)
CYAN = (0, 255, 255)


#game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60

TILESIZE = 64
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE


WALL_IMG = 'buliding\GTA2_TILE_26.bmp'

#player settings
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'garbagetruck/trashmaster_v2.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 50, 50)
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 32