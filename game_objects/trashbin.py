import pygame as pg

class trashbin(pg.sprite.Sprite):
    
    def __init__(self,x,y,img, type):
        super().__init__()
        
        # trashbin type
        self.type = type

        # dimensions
        if type == "small":
            self.width = 4
            self.height = 4
        elif type == "medium":
            self.width = 8
            self.height = 8
        elif type == "large":
            self.width = 16
            self.height = 16
            
        # spawn coords
        self.x = x
        self.y = y
    
        # load trashbin image
        self.image = pg.image.load(img)
        self.image = pg.transform.scale(self.image, (self.x,self.y))
        self.rect = self.image.get_rect()