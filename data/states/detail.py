#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg

class DetailImage(pg.sprite.Sprite):
    def __init__(self, img, position, length, img_cont, name_img, img_length):
    	pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(img, length)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.length = length
        self.img_cont = img_cont
        self.img_length = img_length
        self.name_img = name_img
        self.angle = 0

    def draw_image(self, surf):
        self.img_cont = pg.transform.scale(self.img_cont, self.img_length)
        img_cont = pg.transform.rotate(self.img_cont, self.angle)
        img_rect = img_cont.get_rect()
        img_rect.center = self.rect.center
        surf.blit(img_cont, img_rect)

    def click(self, pos):
        if (pos[0] >= self.rect.left and pos[0] <= self.rect.left + self.length[0]) and (pos[1] >= self.rect.top and pos[1] <= self.rect.top + self.length[1]):
            return True
        else:
            return False

    def rotate(self, angle):
        self.image = pg.transform.rotate(self.image, angle)
        self.angle = angle

    def get_img(self):
        return self.name_img

class DetailText(pg.sprite.Sprite):
    def __init__(self, img, position, length, text, color_text):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(img, length)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.text = text
        self.color_text = color_text
        self.length = length

    def draw_text(self, surf, size, style_font):
        font = pg.font.Font(style_font, size)
        text_surface = font.render(self.text, True, self.color_text)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        surf.blit(text_surface, text_rect)

    def click(self, pos):
        if (pos[0] >= self.rect.left and pos[0] <= self.rect.left + self.length[0]) and (pos[1] >= self.rect.top and pos[1] <= self.rect.top + self.length[1]):
            return True
        else:
            return False

    def set_text(self, new_text):
        self.text = new_text
