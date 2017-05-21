# coding=utf-8
# oryginalna mapa pobrana z https://upload.wikimedia.org/wikipedia/commons/# e/e1/Ising_model_5x5_0.svg,
# zmniejszona manualnie do rozmiarów 550x550 px, nazwa pliku z mapą '5x5.png', wczytywanie w linii 504 kodu źródłowego

TITLE = 'Tic Tac Toe'
CROSS_PNG_PATH = './Sprites/cross.png'
CIRCLE_PNG_PATH = './Sprites/circle.png'
MAP_PNG_PATH = './Sprites/3x3.png'
CROSS_SOUND_PATH = './Sounds/crossSound.mp3'
CIRCLE_SOUND_PATH = './Sounds/circleSound.mp3'
COL = '\033[91m'
ENDC = '\033[0m'
SPACE_LENGTH = 3
SPACES_AMOUNT = 4
BOX_LENGTH = 554
DIMENSION = 3
AMOUNT_OF_BOXES = DIMENSION*DIMENSION
SMALL_BOX_LENGTH = int((BOX_LENGTH - SPACES_AMOUNT * SPACE_LENGTH) / DIMENSION)
THICKNESS_OF_BOX_BORDER = 2  # pixels
THICKNESS = int(10)
LEFT_MOUSE = 0
POS_X = 0
POS_Y = 1
EMPTY = 0
CROSS = 1
CIRCLE = 2
DEPTH = 9
