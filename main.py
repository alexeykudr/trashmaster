import pygame
from map import preparedMap

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

    # event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # end
    pygame.quit()