#coding: utf-8
__author__ = 'thiagowhispher'

# Paths #
PATH_FILE_RESOLUTION = 'data/resolution.txt'

def load_size_screen():
    file_resolution = open(PATH_FILE_RESOLUTION)
    return map(int, file_resolution.read().split(' '))

# Variables #
SIZE_SCREEN = load_size_screen()
ORIGINAL_CAPTION = "Kenney Checkers"
FPS = 120

# Define colors #
BLACK_COLOR = (0  ,   0,   0)
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (115, 205,  75)

# Define local sprite player #
LOCAL_SPRITES_1 = [0, 1, 2]
LOCAL_SPRITES_2 = [5, 6, 7]
