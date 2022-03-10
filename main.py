import pygame
from map import preparedMap
from agent import trashmaster


class WalleGame():
    
    def __init__(self):
        self.SCREEN_SIZE = [512, 512]
        self.BACKGROUND_COLOR = '#ffffff'
        
        pygame.init()
        pygame.display.set_caption('Wall-e')
        
        
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.screen.fill(pygame.Color(self.BACKGROUND_COLOR))
        
        # krata
        self.map = preparedMap(self.SCREEN_SIZE)
        self.screen.blit(self.map, (0,0))
        
    def update_window(self):
        pygame.display.update()
    
    def draw_trashmaster(self, smieciara: trashmaster):
        smieciara_list = pygame.sprite.Group()
        smieciara_list.add(smieciara)
        smieciara_list.draw(self.screen)
        
        

def main():
    game = WalleGame()
    game.update_window()
    
    smieciara_object = trashmaster()
    game.draw_trashmaster(smieciara_object)

    game.update_window()

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
    pygame.quit()
   


if __name__ == '__main__':
    main()