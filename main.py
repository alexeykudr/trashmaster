from calendar import c
from game_objects.player import Player
import pygame as pg
import sys
from os import path
# from agent import trashmaster
# from house import House
from settings import *
from map import map
from map import map_utils
import math

class Game():
    
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Trashmaster")
        self.load_data()
        self.init_game()

    def init_game(self):
        # initialize all variables and do all the setup for a new game

        # sprite groups
        self.roadTiles, self.wallTiles = map.get_tiles()
        self.agentSprites = pg.sprite.Group()

        # player obj
        self.player = Player(self, 32, 100)

        # camera obj
        self.camera = map_utils.Camera(MAP_WIDTH_PX, MAP_HEIGHT_PX)

        # other
        self.draw_debug = False

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'resources/textures')

        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (PLAYER_WIDTH,PLAYER_HEIGHT) )
        
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
        self.agentSprites.update()
        self.camera.update(self.player)
        # pygame.display.update()

    def draw(self):
        #display fps as window title
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))

        #rerender map
        map.render_tiles(self.roadTiles, self.screen, self.camera)
        map.render_tiles(self.wallTiles, self.screen, self.camera, self.draw_debug)

        #rerender additional sprites
        for sprite in self.agentSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
        
        #finally update screen
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
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                clicked_coords = [math.floor(pos[0] / TILESIZE), math.floor(pos[1] / TILESIZE)]
                print(clicked_coords)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.run()
    g.show_go_screen()

