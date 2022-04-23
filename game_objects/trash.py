import pygame as pg

class trash(pg.sprite.Sprite):
    
    def __init__(self,x,y,img, type):
        super().__init__()
        
        self.width=16
        self.height=16

        self.type = type

        self.x = x
        self.y = y
    
        self.image = pg.image.load(img)
        self.image = pg.transform.scale(self.image, (self.x,self.y))
        self.rect = self.image.get_rect()