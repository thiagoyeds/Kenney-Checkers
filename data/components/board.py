#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg

class Board(pg.sprite.Sprite):
    def __init__(self, player_one, player_two):
        pg.sprite.Sprite.__init__(self)
        self.player_one = player_one
        self.player_two = player_two

        #Move Hero
        self.playing = False
        self.hero_select = None
        self.coord_hero_select = False
        self.new_coord_hero = False

        #Define heros of the two players
        self.heros = pg.sprite.Group()
        self.heros_move = pg.sprite.Group()
        self.heros_capture_required = pg.sprite.Group()

    def check_final_game(self):
        enemy = self.player_two.get_heros()
        final_player_one = self.player_one.without_play(self.heros, enemy, 1)
        enemy = self.player_one.get_heros()
        final_player_two = self.player_two.without_play(self.heros, enemy, 2)
        if final_player_one:
            return 2
        if final_player_two:
            return 1
        return 0

    def update_all_heros(self):
        self.heros.empty()
        self.heros.add(self.player_one.get_heros())
        self.heros.add(self.player_two.get_heros())

    def update_hero(self, pos):
        for hero in self.heros_move:
            if hero.equal_coord(pos):
                self.hero_select.set_coord(pos)
                return True
        return False

    def check_capture_required(self, turn):
        if turn == 1:
            enemy = self.player_two.get_heros()
            if self.hero_select == None:
                self.heros_capture_required = self.player_one.check_capture_heros(enemy, self.heros)
            else:
                self.heros_capture_required.empty()
                if len(self.hero_select.capture(enemy, self.heros)):
                    self.heros_capture_required.add(self.hero_select)
        else:
            enemy = self.player_one.get_heros()
            if self.hero_select == None:
                self.heros_capture_required = self.player_two.check_capture_heros(enemy, self.heros)
            else:
                self.heros_capture_required.empty()
                if len(self.hero_select.capture(enemy, self.heros)):
                    self.heros_capture_required.add(self.hero_select)

    def check_hero(self, hero_select):
        if not len(self.heros_capture_required):
            return True
        else:
            x, y = hero_select.get_coord()
            for hero in self.heros_capture_required:
                if hero.equal_coord([x, y]):
                    return True
            return False

    def check_flip_turn(self, turn):
        if turn == 1:
            if self.player_one.get_playing() == 'No capture':
                self.player_one.set_playing('No play')
                self.hero_select = None
                turn = self.flip_turn(turn)
            elif self.player_one.get_playing() == 'Capture':
                if not self.player_one.hero_moving():
                    self.check_capture_required(turn)
                    if not len(self.heros_capture_required):
                        self.player_one.set_playing('No play')
                        self.hero_select = None
                        turn = self.flip_turn(turn)
        else:
            if self.player_two.get_playing() == 'No capture':
                self.player_two.set_playing('No play')
                self.hero_select = None
                turn = self.flip_turn(turn)
            elif self.player_two.get_playing() == 'Capture':
                if not self.player_two.hero_moving():
                    self.check_capture_required(turn)
                    if not len(self.heros_capture_required):
                        self.player_two.set_playing('No play')
                        self.hero_select = None
                        turn = self.flip_turn(turn)
        return turn

    def play(self, pos, turn):
        # Case hero is select
        if self.playing:
            if self.update_hero(pos):
                self.new_coord_hero = self.hero_select.get_coord()
                self.playing = False
                self.heros_move.empty()
                if turn == 1:
                    if len(self.heros_capture_required):
                        self.player_one.set_playing('Capture')
                        self.hero_select.set_moving(True)
                    else:
                        self.player_one.set_playing('No capture')
                        self.hero_select.set_moving(True)
                else:
                    if len(self.heros_capture_required):
                        self.player_two.set_playing('Capture')
                        self.hero_select.set_moving(True)
                    else:
                        self.player_two.set_playing('No capture')
                        self.hero_select.set_moving(True)
                self.heros_capture_required.empty()
                return self.heros_move

        if turn == 1:
            hero = self.player_one.search_hero(pos)
            enemy = self.player_two.get_heros()
        else:
            hero = self.player_two.search_hero(pos)
            enemy = self.player_one.get_heros()
        if hero[0]:
            if self.check_hero(hero[1]):
                self.hero_select = hero[1]
                self.playing = True
                self.coord_hero_select = self.hero_select.get_coord()
                self.heros_move = self.hero_select.move(self.heros, enemy, turn)
            else:
                self.heros_move.empty()
        else:
            self.playing = False
            self.hero_select = None
            self.heros_move.empty()
        return self.heros_move

    def analisy_capture(self, turn, heros_player_one, heros_player_two):
        if turn == 1:
            pg.sprite.groupcollide(heros_player_two, heros_player_one, True, False)
        else:
            pg.sprite.groupcollide(heros_player_one, heros_player_two, True, False)

    def flip_turn(self, turn):
        if turn == 1: return 2
        else: return 1

    def get_color_hero(self, player):
        if player == 1:
            return self.player_one.get_color_hero()
        else:
            return self.player_two.get_color_hero()

    def get_playing(self):
        return self.playing

    def get_heros(self):
        return self.heros
