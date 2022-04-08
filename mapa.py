import pygame as pg
import pytmx


# config
# TILE_SIZE = 16

# def preparedMap(screenSize):
#     tileImage = pg.image.load('tile1.png')
#     surface = pg.Surface(screenSize)

#     for x in range(0, screenSize[0], TILE_SIZE):
#         for y in range(0, screenSize[1], TILE_SIZE):
#             surface.blit(tileImage, (x, y))
#     return surface

class TiledMap:
    # loading file
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    # rendering map
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tilewidth))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface