#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
from commom import Commom
from queen import Queen

class Player(pg.sprite.Sprite):
    def __init__(self, color_hero, sprites, num_player, margin, number_divide):
        pg.sprite.Sprite.__init__(self)
        self.color_hero = color_hero
        self.heros = pg.sprite.Group()
        self.num_player = num_player
        self.margin = margin
        self.number_divide = number_divide
        self.playing = 'No capture'
        for linha in sprites:
            for coluna in range(8):
                if (not linha % 2 and not coluna % 2) or (linha % 2 and coluna % 2):
                    hero = Commom([coluna, linha], color_hero, num_player, margin, number_divide)
                    self.heros.add(hero)

    def without_play(self, all_heros, enemy, player):
        play = pg.sprite.Group()
        for hero in self.heros:
            play = hero.move(all_heros, enemy, player)
            if len(play):
                return False
        return True

    def hero_moving(self):
        for hero in self.heros:
            if hero.get_moving():
                return True
        return False

    def check_capture_heros(self, enemy, all_heros):
        heros_capture_required = pg.sprite.Group()
        for hero in self.heros:
            if len(hero.capture(enemy, all_heros)):
                heros_capture_required.add(hero)
        return heros_capture_required

    def change_type_heros(self):
        for hero in self.heros:
            coord = hero.get_coord()
            if self.color_hero == hero.get_color_hero():
                if (self.num_player == 1 and hero.get_coord()[1] == 7) or (self.num_player == 2 and hero.get_coord()[1] == 0):
                    hero.destroy()
                    new_hero = Queen(coord, self.color_hero, self.num_player, (self.margin), self.number_divide)
                    self.heros.add(new_hero)

    def search_hero(self, pos):
        for hero in self.heros:
            if hero.equal_coord(pos):
                return [True, hero]
        return [False, None]

    def set_playing(self, opc):
        self.playing = opc

    def get_color_hero(self):
        return self.color_hero

    def get_playing(self):
        return self.playing

    def get_heros(self):
        return self.heros

    def how_many_heros(self):
        return len(self.heros)
