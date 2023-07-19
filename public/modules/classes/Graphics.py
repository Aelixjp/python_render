import pygame

from .Utils import createRect, createVector

class Graphics:

    def __init__(self, screen) -> None:
        self.screen = screen

    def drawPixel(self, color, x, y):
        self.screen.set_at((x, y), color)

    def drawRect(self, color, outline, x, y, width, height = -1):
        height = width if height == -1 else height
        mrect = createRect((x, y, width, height))

        pygame.draw.rect(self.screen, color, mrect, outline)

    def drawCircle(self, color, outline, pos, rad):
        vpos = createVector(pos)

        pygame.draw.circle(self.screen, color, vpos, rad, outline)

    def drawTriangle(self, color, point_1, point_2, point_3):
        self.drawPolygon(color, (point_1, point_2, point_3))

    def drawTriangle(self, color, x, y, size, triangle_mod = 'ISOC', inverted = False):
        
        if triangle_mod == 'ISOC':
            point_1 = (x             ,        y) if not inverted else (x             , y - size)
            point_2 = (x + (size / 2), y - size) if not inverted else (x + (size / 2), y       )
            point_3 = (x + size      ,        y) if not inverted else (x + size      , y - size)

            self.drawPolygon(color, (point_1, point_2, point_3))

        elif triangle_mod == 'EQ':
            point_1 = (x             ,              y) if not inverted else (x             , (y - (size / 2)))
            point_2 = (x + (size / 2), y - (size / 2)) if not inverted else (x + (size / 2), y               )
            point_3 = (x + size      ,              y) if not inverted else (x + size      , (y - (size / 2)))

            self.drawPolygon(color, (point_1, point_2, point_3))

        else:
            print("Aviso: El triangulo no posee un modo correcto, no será dibujado!")

    def drawPolygon(self, color, outline, points):
        pygame.draw.polygon(self.screen, color, points, outline)