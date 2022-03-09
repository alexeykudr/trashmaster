import pygame

from agent import trashmaster



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

smieciara1 = trashmaster()
smieciara_list = pygame.sprite.Group()
smieciara_list.add(smieciara1)
smieciara_list.draw(screen)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   

pygame.quit()
