import pygame
from map import preparedMap
from agent import trashmaster
from house import House

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
    
    def draw_object(self, drawable_object, pos):
        # pos => (x, y)
        # drawable object must have .image field inside class
        self.screen.blit(drawable_object.image, pos )

    def reloadMap(self):
        self.screen.fill(pygame.Color(self.BACKGROUND_COLOR))
        self.screen.blit(self.map, (0,0))
        
def main():
    game = WalleGame()
    game.update_window()
    
    smieciara_object = trashmaster(16,16,"./resources/textures/garbagetruck/trashmaster_blu.png")
    game.draw_object(smieciara_object, (0, 0))

    house_object = House(20, 20)
    # Test draw house object
    game.draw_object(house_object, (20,20))

    game.update_window()

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game.reloadMap()
                game.draw_object(smieciara_object, 
                                        smieciara_object.movement(event.key, 16))
                
                game.update_window()

    pygame.quit()
   


if __name__ == '__main__':
    main()