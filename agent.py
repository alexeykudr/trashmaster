import pygame.image

class trashmaster(pygame.sprite.Sprite):
    def __init__(self,x,y,img,vel):
        super().__init__()
        
        self.x=x
        self.y=y
        self.img = img
        self.velocity = vel
    
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (self.x,self.y))
        self.rect = self.image.get_rect()
