import pygame as pg
import pygame.image
from settings import *
from random import uniform
from map import collide_hit_rect

vec = pg.math.Vector2


def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)


    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.wallTiles, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.wallTiles, 'y')
        self.rect.center = self.hit_rect.center

class Dump(pg.sprite.Sprite):
    # wysypisko
    def __init__(self):
        super().__init__()   
        self.glass = []
        self.paper = []
        self.bio = []
        self.other_trash = []
class trash(pg.sprite.Sprite):
    
    def __init__(self,x,y,img, type):
        super().__init__()
        
        self.width=16
        self.height=16

        self.type = type

        self.x = x
        self.y = y
    
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (self.x,self.y))
        self.rect = self.image.get_rect()
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
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (self.x,self.y))
        self.rect = self.image.get_rect()

class trashmaster(pg.sprite.Sprite):
    
    def __init__(self,x,y,img):
        super().__init__()
        
        self.width=x
        self.height=y

        self.x = 0
        self.y = 0
    
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
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

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
