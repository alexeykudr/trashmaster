import pygame as pg
from enum import Enum

from map.tile import Tile

class Waste_Type(Enum):
    BIO = 0
    GLASS = 1
    PLASTIC = 2
    PAPER = 3
    MIX = 4

    def __int__(self):
        return self.value
class Trashbin(Tile):
    def __init__(self, img, x, y, width, height, waste_type: Waste_Type):
        super().__init__(img, x, y, width, height)
        
        self.waste_type = waste_type
        self.days_after_pickup = 0
        self.max_capacity = 100
        self.used_capacity = 0
        self.access = True
