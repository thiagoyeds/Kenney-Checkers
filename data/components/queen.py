#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
from .. import setup as stp

# Define moves #
# Player One (Type Hero Commom)#
x1 = [1, -1]
y1 = [1, 1]

# Player Two (Type Hero Commom)#
x2 = [1, -1]
y2 = [-1, -1]

def abs(x):
    if x < 0:
        return x * (-1)
    else:
        return x

class Queen(pg.sprite.Sprite):
    def __init__(self, coord, color, num_player, margin, number_divide):
        pg.sprite.Sprite.__init__(self)
        self.color_hero = color
        self.number_divide = number_divide
        self.image = pg.transform.scale(stp.PLAYERS[color], (int(number_divide*0.8), int(number_divide*0.8)))
        self.rect = self.image.get_rect()
        self.center_hero = self.number_divide/2
        self.rect.center = (int(coord[0] * self.number_divide) + margin[0] + self.center_hero, coord[1] * self.number_divide + margin[1] + self.center_hero)
        self.coord = coord
        self.num_player = num_player
        self.speedy = 0
        self.speedx = 0
        self.margin = margin
        self.moving = False

    def direct_move(self, player):
        if player == 1:
            return x1, y1
        else:
            return x2, y2

    def direct_capture(self, hero, enemy):
        if hero[1] < enemy[1]:
            if hero[0] < enemy[0]:
                return [ 1,  1]
            else:
                return [-1,  1]
        else:
            if hero[0] < enemy[0]:
                return [ 1, -1]
            else:
                return [-1, -1]

    def move(self, all_heros, enemys, player):
        hero_move = pg.sprite.Group()
        hero_move.add(self.capture(enemys, all_heros))
        if not len(hero_move):
            dm_x, dm_y = self.direct_move(player)
            for c in range(-7, 8):
                for i in range(2):
                    cd_x = self.coord[0] + (dm_x[i] * c)
                    cd_y = self.coord[1] + (dm_y[i] * c)
                    if self.verify(cd_x, cd_y, all_heros):
                        if not self.collader_outhers_heros(self.coord, [cd_x, cd_y], all_heros):
                            hero = Queen([cd_x, cd_y], self.color_hero+'_ghost', self.num_player, self.margin, self.number_divide)
                            hero_move.add(hero)
        return hero_move

    def verify(self, x, y, all_heros):
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            for hero in all_heros:
                if hero.equal_coord([x, y]):
                    return False
            return True
        else:
            return False

    def capture(self, enemys, all_heros):
        hero_move = pg.sprite.Group()
        for enemy in enemys:
            coord_enemy = enemy.get_coord()
            if coord_enemy[0] > 0 and coord_enemy[0] < 7 and coord_enemy[1] > 0 and coord_enemy[1] < 7:
                if abs(self.coord[0] - coord_enemy[0]) == abs(self.coord[1] - coord_enemy[1]):
                    x, y = self.direct_capture(self.coord, coord_enemy)
                    cd_x = (coord_enemy[0] + x)
                    cd_y = (coord_enemy[1] + y)
                    if self.verify(cd_x, cd_y, all_heros):
                        if not self.collader_outhers_heros(self.coord, [coord_enemy[0] - x, coord_enemy[1] - y], all_heros):
                            hero = Queen([cd_x, cd_y], self.color_hero+'_ghost', self.num_player, self.margin, self.number_divide)
                            hero_move.add(hero)
        return hero_move

    def collader_outhers_heros(self, coord_ini, coord_fin, all_heros):
        coord = self.direct_capture(coord_ini, coord_fin)
        path = [coord_ini[0] + coord[0], coord_ini[1] + coord[1]]
        coord_fin = [coord_fin[0] + coord[0], coord_fin[1] + coord[1]]
        while path != coord_fin:
            for hero in all_heros:
                if hero.equal_coord(path):
                    return True
            path = [path[0] + coord[0], path[1] + coord[1]]
        return False

    def equal_coord(self, coord):
        if self.coord == coord: return True
        else: return False

    def set_moving(self, opc):
        self.moving = opc

    def set_coord(self, pos):
        move_sound = pg.mixer.Sound(stp.SOUNDS['move'])
        move_sound.play()
        self.speedx, self.speedy = self.direct_capture(self.coord, pos)
        self.speedx *= 2
        self.speedy *= 2
        self.coord = pos

    def destroy(self):
        self.kill()

    def get_num_player(self):
        return self.num_player

    def get_color_hero(self):
        return self.color_hero

    def get_coord(self):
        return self.coord

    def get_moving(self):
        if self.rect.center == self.cal_center():
            self.moving = False
        return self.moving

    def cal_center(self):
        return (int(self.coord[0] * self.number_divide) + self.center_hero + self.margin[0], int(self.coord[1] * self.number_divide) + self.center_hero + self.margin[1])

    def update(self):
        if self.rect.center != self.cal_center():
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        else:
            self.speedx = 0
            self.speedy = 0
