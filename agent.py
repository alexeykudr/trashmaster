import pygame.image


class trashmaster(pygame.sprite.Sprite):

    def __init__(self, x, y, img):
        super().__init__()

        self.width = x
        self.height = y

        self.x = 0
        self.y = 0

        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def movement(self, key, vel):
        if key == pygame.K_LEFT:
            self.x -= vel

        if key == pygame.K_RIGHT:
            self.x += vel

        if key == pygame.K_UP:
            self.y -= vel

        if key == pygame.K_DOWN:
            self.y += vel
        return (self.x, self.y)

    def move_up(self):
        self.y -= 64

    def move_down(self):
        self.y += 64

    def move_right(self):
        self.x += 64

    def move_left(self):
        self.x -= 64
