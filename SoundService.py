import pygame

from Config import CROSS_SOUND_PATH, CIRCLE_SOUND_PATH


def playCrossSound():
    pygame.mixer.music.load(CROSS_SOUND_PATH)
    pygame.mixer.music.play(0)


def playCircleSound():
    pygame.mixer.music.load(CIRCLE_SOUND_PATH)
    pygame.mixer.music.play(0)
