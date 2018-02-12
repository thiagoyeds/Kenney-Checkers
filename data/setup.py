#coding: utf-8
__author__ = 'thiagowhispher'

import os
import pygame as pg
import constants as c

def open_back(value):
    if value:
        move_sound = pg.mixer.Sound(SOUNDS['open'])
        move_sound.play()
    else:
        move_sound = pg.mixer.Sound(SOUNDS['back'])
        move_sound.play()
    pg.time.wait(1000)

def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', '.jpg')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics

def load_all_sfx(directory, accept=('.mp3', '.wav', '.ogg')):
    songs = {}
    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs

def load_all_fonts(directory, accept=('.ttf')):
    return load_all_sfx(directory, accept)

# Initialize pygame #
pg.init()
pg.mixer.init()
pg.font.init()

# Create windows and outhers tools #
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SIZE_SCREEN)
SCREEN_RECT = SCREEN.get_rect()
CLOCK = pg.time.Clock()

# Define path #
BOARDS = load_all_gfx(os.path.join("resources","graphics","boards"))
PLAYERS = load_all_gfx(os.path.join("resources","graphics","players"))
SOUNDS = load_all_sfx(os.path.join("resources", "sound"))
BUTTONS = load_all_gfx(os.path.join("resources","graphics", "buttons"))
FONTS = load_all_fonts(os.path.join("resources", "fonts"))
BACK = load_all_gfx(os.path.join("resources", "graphics", "background"))
NUMBERS = load_all_gfx(os.path.join("resources", "graphics", "numbers"))
HEROS = load_all_gfx(os.path.join("resources", "graphics", "heros"))
REFERENCES = load_all_gfx(os.path.join("references"))
ICON = load_all_gfx(os.path.join("resources", "icon"))
