#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import SoundService
from Coordinates import Coordinates
from Config import DIMENSION, BOX_LENGTH, SMALL_BOX_LENGTH, SPACE_LENGTH, LEFT_MOUSE, POS_X, POS_Y, EMPTY, CIRCLE, CROSS
from MinMaxStrategy import MinMaxStrategy
from View import View
from MapMatrix import MapMatrix


def main():
    gameMatrix = MapMatrix(DIMENSION)
    view = View()
    view.draw(gameMatrix.matrix)
    ai = MinMaxStrategy(gameMatrix)
    view.draw(gameMatrix.matrix)
    while True:
        i = pygame.event.wait()
        if i.type == pygame.QUIT:
            sys.exit(0)

        if pygame.mouse.get_pressed()[LEFT_MOUSE]:
            pos = pygame.mouse.get_pos()
            wsp_x = int(pos[POS_X] / (SMALL_BOX_LENGTH + SPACE_LENGTH))
            wsp_y = int(pos[POS_Y] / (SMALL_BOX_LENGTH + SPACE_LENGTH))
            if pos[POS_X] > BOX_LENGTH or pos[POS_X] < 0 or pos[POS_Y] > BOX_LENGTH or pos[POS_Y] < 0 or gameMatrix.matrix[wsp_y][wsp_x] != EMPTY:
                continue
            else:
                gameMatrix.markCrossOn(Coordinates(wsp_y, wsp_x))
                view.draw(gameMatrix.matrix)
                SoundService.playCrossSound()

                if ai.hasWon(CROSS):
                    sys.exit("Wygrales!")
                elif (not ai.hasWon(CROSS)) and gameMatrix.checkIfMapFull():
                    sys.exit("Remis!")

                ai.doBestMove(gameMatrix)
                view.draw(gameMatrix.matrix)
                SoundService.playCircleSound()

                if ai.hasWon(CIRCLE):
                    sys.exit("Przegrales!")
                elif (not ai.hasWon(CIRCLE)) and gameMatrix.checkIfMapFull():
                    sys.exit("Remis!")


main()
