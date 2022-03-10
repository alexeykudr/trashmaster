import pygame
from map import preparedMap
from agent import trashmaster
# import os
# os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()

#config
SCREEN_SIZE = [512, 512]
BACKGROUND_COLOR = '#ffffff'

if __name__ == '__main__':

    pygame.init()

    # tytul okna
    pygame.display.set_caption('Wall-e')

    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(pygame.Color(BACKGROUND_COLOR))

    # krata
    map = preparedMap(SCREEN_SIZE)
    screen.blit(map, (0,0))

    # update okna
    pygame.display.update()

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
