import pygame.image


class trashmaster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        
        self.images = []
        self.image = pygame.image.load("resources/textures/trashmaster_blu.png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.images.append(self.image)
        self.rect = self.image.get_rect()

        garbagetruck_list = pygame.sprite.Group()
