from asyncio import sleep
from calendar import c
from random import randint
import time
import os
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
from path_search_algorthms import a_star, a_star_utils
from decision_tree import decisionTree
from NeuralNetwork import prediction
from game_objects.trash import Trash

from game_objects import aiPlayer
import itertools


def getTree():
    tree = decisionTree.tree()
    decisionTree.tree_as_txt(tree)
    # decisionTree.tree_to_png(tree)
    decisionTree.tree_to_structure(tree)
    drzewo = decisionTree.tree_from_structure('./decision_tree/tree_model')
    # print("Dla losowych danych predykcja czy wziąć kosz to: ")
    # dec = decisionTree.decision(drzewo, *(4,1,1,1))
    # print('---')
    # print(f"decision is{dec}")
    # print('---')

    return drzewo


class Game():

    def __init__(self):
        pg.init()
        pg.font.init()
        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(FPS) / 333.0
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Trashmaster")
        self.load_data()
        self.init_game()
        # because dont work without data.txt
        # self.init_bfs()
        # self.init_a_star()
        self.t = aiPlayer.aiPlayer(self.player, game=self)

        
    def get_actions_by_coords(self,x,y):
        pos = (x,y)
        offset_x, offset_y = self.camera.offset()
        clicked_coords = [math.floor(pos[0] / TILESIZE) - offset_x, math.floor(pos[1] / TILESIZE) - offset_y]
        actions = a_star.search_path(math.floor(self.player.pos[0] / TILESIZE),
                                        math.floor(self.player.pos[1] / TILESIZE), self.player.rotation(),
                                        clicked_coords[0], clicked_coords[1], self.mapArray)
        return actions

    def init_game(self):
        # initialize all variables and do all the setup for a new game

        self.text_display = ''

        # sprite groups and map array for calculations
        (self.roadTiles, self.wallTiles, self.trashbinTiles), self.mapArray = map.get_tiles()
        self.trashDisplay = pg.sprite.Group()
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
        for i in range(len(path) - 1, 0, -1):
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

    def init_decision_tree(self):
         # logika pracy z drzewem
        self.positive_decision = []
        self.negative_decision = []

        for i in self.trashbinTiles:
            atrrs_container = i.get_attributes()
            x, y = i.get_coords()
            dec = decisionTree.decision(getTree(), *atrrs_container)
            if dec[0] == 1:
                self.positive_decision.append(i)
            else:
                self.negative_decision.append(i)
        
        # print('positive actions')
        # for i in self.positive_actions:
        #     print('----')
        #     print(i)
        #     print('----')

        print('positive actions')
        print(len(self.positive_decision))
        for i in self.positive_decision:
            # print(i.get_coords())
            trash_x, trash_y = i.get_coords()
            action = self.get_actions_by_coords(trash_x, trash_y)
            self.t.startAiController(action)

            print('')
            print('--rozpoczecie sortowania smietnika--')
            dir = "./resources/trash_dataset/test/all"
            files = os.listdir(dir)
            for i in range(0, 10):
                random = randint(0, 48)
                file = files[random]
                result = prediction.getPrediction(dir + '/' +file, 'trained_nn_20.pth')
                img = pg.image.load(dir + '/' +file).convert_alpha()
                img = pg.transform.scale(img, (128, 128))
                trash = Trash(img, 0, 0, 128, 128)
                self.trashDisplay.add(trash)
                self.text_display = result
                self.draw()
                print(result + '   ' + file)
                pg.time.wait(1000)
            self.text_display = ''
            self.draw()

        # print(self.positive_actions[0])

        # self.t.startAiController(self.positive_actions[0])
        

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'resources/textures')

        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

    def run(self):
        # game loop - set self.playing = False to end the game 
        self.playing = True
        self.init_decision_tree()
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
        # display fps as window title
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))

        # rerender map
        map.render_tiles(self.roadTiles, self.screen, self.camera)
        map.render_tiles(self.wallTiles, self.screen, self.camera, self.debug_mode)
        map.render_tiles(self.trashbinTiles, self.screen, self.camera)
        map.render_tiles(self.trashDisplay, self.screen, self.camera)

        # draw text
        text_surface = pg.font.SysFont('Comic Sans MS', 30).render(self.text_display, False, (0,0,0))
        self.screen.blit(text_surface, (0,128))

        # rerender additional sprites
        for sprite in self.agentSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.debug_mode:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)

        # finally update screen
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
                offset_x, offset_y = self.camera.offset()
                clicked_coords = [math.floor(pos[0] / TILESIZE) - offset_x, math.floor(pos[1] / TILESIZE) - offset_y]
                actions = a_star.search_path(math.floor(self.player.pos[0] / TILESIZE),
                                             math.floor(self.player.pos[1] / TILESIZE), self.player.rotation(),
                                             clicked_coords[0], clicked_coords[1], self.mapArray)
                # print(actions)
                
                if (actions != None):
                    self.t.startAiController(actions)

                

# create the game object

if __name__ == "__main__":
    g = Game()
    
    g.run()
    g.show_go_screen()