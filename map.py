import pygame

# config
TILE_SIZE = 16

def preparedMap(screenSize):
    tileImage = pygame.image.load('tile1.png')
    surface = pygame.Surface(screenSize)

    for x in range(0, screenSize[0], TILE_SIZE):
        for y in range(0, screenSize[1], TILE_SIZE):
            surface.blit(tileImage, (x, y))
    return surface