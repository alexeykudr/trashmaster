import pygame as pg
vec = pg.math.Vector2

class aiPlayer():
    def __init__(self, player, game):
        self.player = player
        self.game = game
        self.angle = 0

    def rotateAiPlayer(self, d: str):
        if d == 'left':
            print('in left')
            self.direction -= 90
        if d == 'right':
            self.direction += 90

    def moveAiPlayer(self):
        for i in range(64 * 1):
            self.player.pos += vec(1, 0).rotate(self.angle)
            self.player.rect.center = self.player.pos
            # print(f'START COORDS: {x_s, x_bias}; CURRENT AGENT COORDS: {self.player.get_actual_coords()}')
            self.game.update()
            self.player.update()
            self.game.draw()
            print(self.player.get_actual_coords())
            
            

    def turn_left(self):
        self.player.rot -= 90
        self.angle -= 90

    def turn_right(self):
        self.player.rot += 90
        self.angle += 90

    def startAiController(self):
        actions = ['right', 'straight', 'straight', 'left', 'straight'
                   ]
        for action in actions:
            if action == 'straight':
                self.moveAiPlayer()
                print(f'ROT IS {self.player.rot}')
            if action == 'right':
                self.turn_right()
            if action == 'left':
                self.turn_left()