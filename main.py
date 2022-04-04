import pygame as pg
import sys
from os import path
from map import *
# from agent import trashmaster
# from house import House
from sprites import *
from settings import *

class Game():
    
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Trashmaster")
        self.clock = pg.time.Clock()
        self.load_data()
    
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'resources/textures')
        map_folder = path.join(img_folder, 'map')
        self.map = TiledMap(path.join(map_folder, 'roads.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (PLAYER_WIDTH,PLAYER_HEIGHT) )
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

    def new(self):
        # initialize all variables and do all the setup for a new game

        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

        # self.screen.blit(self.map_img, (0,0))
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
        
        #self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))

    def run(self):
        # game loop - set self.playing = False to end the game 
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()
    
    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        # pygame.display.update()
    
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))


    # def draw(self, drawable_object, pos):
    #     # pos => (x, y)
    #     # drawable object must have .image field inside class
    #     self.screen.blit(drawable_object.image, pos )

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)
        
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    # def reloadMap(self):
    #      #self.screen.fill(pygame.Color(self.BACKGROUND_COLOR))
    #      self.screen.blit(self.map_img, (0,0))
        
# def main():
#     game = WalleGame()
#     game.update_window()
    
#     smieciara_object = trashmaster(16,16,"./resources/textures/garbagetruck/trashmaster_blu.png")
#     game.draw_object(smieciara_object, (100, 100))

#     #house_object = House(20, 20)
#     # Test draw house object
#     #game.draw_object(house_object, (20,20))

#     game.update_window()

#     running = True
    
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 game.reloadMap()
#                 game.draw_object(smieciara_object, smieciara_object.movement(event.key, 16))
                
#                 game.update_window()

#     pygame.quit()
# if __name__ == '__main__':
#     main()


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

