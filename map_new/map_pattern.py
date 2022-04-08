import os
import pygame as pg

HERE_DIR = os.path.abspath(os.path.dirname(__file__))
TEXTURES_DIR = HERE_DIR.rpartition(os.sep)[0]+"\\resources\\textures"

ROAD_DIR = TEXTURES_DIR+"\\road\\"
BUILDING_DIR = TEXTURES_DIR+"\\buliding\\"

def loadImg(path):
    return pg.image.load(path)

def getPattern():
    return {
        0: loadImg(ROAD_DIR+"GTA2_TILE_257.bmp"),
        1: loadImg(BUILDING_DIR+"GTA2_TILE_187.bmp"),
    }