# coding=utf-8
import pygame
from Config import SPACE_LENGTH, SMALL_BOX_LENGTH, DIMENSION, BOX_LENGTH, CIRCLE, \
    CROSS, THICKNESS_OF_BOX_BORDER, TITLE, CROSS_PNG_PATH, CIRCLE_PNG_PATH, MAP_PNG_PATH


class View:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((BOX_LENGTH, BOX_LENGTH))
        pygame.display.set_caption(TITLE)
        self.crossPNG = pygame.image.load(CROSS_PNG_PATH)
        self.circlePNG = pygame.image.load(CIRCLE_PNG_PATH)
        self.mapa = pygame.image.load(MAP_PNG_PATH)
        self.screen = pygame.display.get_surface()
        self.screen.blit(self.mapa, (0, 0))

    def drawCross(self, x, y):
        dimX = SPACE_LENGTH + x * (SMALL_BOX_LENGTH + SPACE_LENGTH)+THICKNESS_OF_BOX_BORDER
        dimY = SPACE_LENGTH + y * (SMALL_BOX_LENGTH + SPACE_LENGTH)+THICKNESS_OF_BOX_BORDER
        self.screen.blit(self.crossPNG, (dimX, dimY))

    def drawCircle(self, x, y):
        dimX = SPACE_LENGTH + x * (SMALL_BOX_LENGTH + SPACE_LENGTH)+THICKNESS_OF_BOX_BORDER
        dimY = SPACE_LENGTH + y * (SMALL_BOX_LENGTH + SPACE_LENGTH)+THICKNESS_OF_BOX_BORDER
        self.screen.blit(self.circlePNG, (dimX, dimY))

    def draw(self, tab):
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if tab[i][j] == CROSS:
                    self.drawCross(j, i)
                elif tab[i][j] == CIRCLE:
                    self.drawCircle(j, i)
                else:
                    pass
        pygame.display.flip()
