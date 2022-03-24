import pygame.image

class trashbin(pygame.sprite.Sprite):
    
    def __init__(self,x,y,img, type):
        super().__init__()
        
        # dimensions
        self.width = 16
        self.height = 16

        # trashbin type
        self.type = type

        # spawn coords
        self.x = x
        self.y = y
    
        # load trashbin image
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (self.x,self.y))
        self.rect = self.image.get_rect()
