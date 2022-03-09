import pygame
pygame.init()

pygame.display.set_caption('Wall-e')

screen = pygame.display.set_mode([512, 512])
screen.fill(pygame.Color('#ffffff'))


tileImage = pygame.image.load('tile1.png')

surfaceSize = width, height = (512, 512)
surface = pygame.Surface(surfaceSize)

for x in range(0, 512, 16):
    for y in range(0, 512, 16):
        surface.blit(tileImage, (x, y))

screen.blit(surface, (0,0))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   

pygame.quit()