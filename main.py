from calendar import c
from game_objects.player import Player
import pygame as pg
import sys
from os import path
import math
from map import *
from settings import *
from map import map
from map import map_utils
from path_search_algorthms import bfs
from path_search_algorthms import a_star


from game_objects import aiPlayer
class Game():

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Trashmaster")
        self.load_data()
        self.init_game()
        # because dont work without data.txt
        # self.init_bfs()
        self.init_a_star()

        self.dt = self.clock.tick(FPS) / 1000.0

    def init_game(self):
        # initialize all variables and do all the setup for a new game

        # sprite groups and map array for calculations
        (self.roadTiles, self.wallTiles), self.mapArray = map.get_tiles()
        self.agentSprites = pg.sprite.Group()

        # player obj
        self.player = Player(self, 32, 32)

        # camera obj
        self.camera = map_utils.Camera(MAP_WIDTH_PX, MAP_HEIGHT_PX)

        # other
        self.debug_mode = False

    def init_bfs(self):
        start_node = (0, 0)
        target_node = (18, 18)
        find_path = bfs.BreadthSearchAlgorithm(start_node, target_node, self.mapArray)
        path = find_path.bfs()
        # print(path)
        realPath = []
        nextNode = target_node
        for i in range(len(path)-1, 0, -1):
            node = path[i]
            if node[0] == nextNode:
                realPath.insert(0, node[0])
                nextNode = node[1]
        print(realPath)

    def init_a_star(self):
        # szukanie sciezki na sztywno i wyprintowanie wyniku (tablica stringow)
        start_x = 0
        start_y = 0
        target_x = 6
        target_y = 2
        path = a_star.search_path(start_x, start_y, target_x, target_y, self.mapArray)
        print(path)

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
        map.render_tiles(self.wallTiles, self.screen, self.camera, self.debug_mode)

        #rerender additional sprites
        for sprite in self.agentSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.debug_mode:
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
                    self.debug_mode = not self.debug_mode
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                clicked_coords = [math.floor(pos[0] / TILESIZE), math.floor(pos[1] / TILESIZE)]
                actions = a_star.search_path(math.floor(self.player.pos[0] / TILESIZE), math.floor(self.player.pos[1] / TILESIZE), clicked_coords[0], clicked_coords[1], self.mapArray)
                print(actions)
                t = aiPlayer.aiPlayer(self.player, game=self)
                t.startAiController(actions=actions)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object

if __name__ == "__main__":
    g = Game()
    g.show_start_screen()

    g.run()
    g.show_go_screen()