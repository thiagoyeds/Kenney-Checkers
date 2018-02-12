#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
from .. import setup as stp

class ButtonImage(pg.sprite.Sprite):
    def __init__(self, id_button, img, position, length, img_cont, name_img, img_length):
        pg.sprite.Sprite.__init__(self)
        self.image_orig = img
        self.image = pg.transform.scale(img, length)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = position
        self.length = length
        self.img_cont = img_cont
        self.img_length = img_length
        self.name_img = name_img
        self.id = id_button
        self.up = 20
        self.length_select_1 = (self.length[0] + self.up, self.length[1] + self.up)
        self.length_select_2 = (self.img_length[0] + self.up, self.img_length[1] + self.up)
        self.select = False

    def draw_image(self, surf):
        if self.select: img_cont = pg.transform.scale(self.img_cont, self.length_select_2)
        else: img_cont = pg.transform.scale(self.img_cont, self.img_length)
        img_rect = img_cont.get_rect()
        img_rect.center = self.rect.center
        surf.blit(img_cont, img_rect)

    def up_lower_button(self, up_lower):
        if up_lower:
            self.image = pg.transform.scale(self.image_orig, self.length_select_1)
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            self.select = True
        else:
            self.image = pg.transform.scale(self.image_orig, self.length)
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            self.select = False

    def set_up(self, new_up):
        self.up = new_up
        self.length_select_2 = (self.img_length[0] + self.up, self.img_length[1] + self.up)

    def set_image(self, new_img):
        self.img_cont = new_img

    def click(self, pos):
        if (pos[0] >= self.rect.left and pos[0] <= self.rect.left + self.length[0]) and (pos[1] >= self.rect.top and pos[1] <= self.rect.top + self.length[1]):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def get_img(self):
        return self.name_img

class ButtonText(pg.sprite.Sprite):
    def __init__(self, id_button, img, position, length, text, color_text):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(img, length)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = position
        self.text = text
        self.color_text = color_text
        self.length = length
        self.id = id_button

    def draw_text(self, surf, size, style_font):
        font = pg.font.Font(style_font, size)
        text_surface = font.render(self.text, True, self.color_text)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        surf.blit(text_surface, text_rect)

    def set_color_text(self, new_color):
        self.color_text = new_color

    def set_image(self, new_image):
        self.image = pg.transform.scale(new_image, self.length)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def click(self, pos):
        if (pos[0] >= self.rect.left and pos[0] <= self.rect.left + self.length[0]) and (pos[1] >= self.rect.top and pos[1] <= self.rect.top + self.length[1]):
            return True
        else:
            return False

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id
