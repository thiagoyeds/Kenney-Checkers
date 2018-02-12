#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
from button import ButtonText
from detail import DetailImage
from .. import setup as stp
from .. import constants as c

class Openingscreen:
    def __init__(self, resolution_screen):
        # Create group buttons
        self.buttons_text = pg.sprite.Group()
        self.details_image = pg.sprite.Group()
        # Set resolution screen #
        pg.display.set_icon(stp.ICON['kenney_icon'])
        self.screen = pg.display.set_mode(resolution_screen)
        self.resolution_screen = resolution_screen
        self.width_screen = resolution_screen[0]
        self.height_screen = resolution_screen[1]
        # Variables #
        self.background = pg.transform.scale(stp.BACK['background'], resolution_screen)
        self.background_rect = self.background.get_rect()
        self.proporcao = self.width_screen / 1280.0
        # Size of objects #
        self.size_detail_kenney = (int(353 * self.proporcao), int(141 * self.proporcao))
        # Radius healding Kenney #
        if self.proporcao == 1:
            self.radius_detail = 300
        else:
            self.radius_detail = 250

    def build(self):
        # Details #
        kenney_logo = DetailImage(stp.BACK['paperwhite'], (self.width_screen/2, self.height_screen/2), (0, 0), stp.BACK['kenney'], 'kenney', self.size_detail_kenney)

        # Add details in Group #
        self.details_image.add(kenney_logo)

    def draw_image(self):
        for detail in self.details_image:
            detail.draw_image(self.screen)

    def draw_screen(self):
        self.screen.fill(c.GREEN_COLOR)
        self.screen.blit(self.background, self.background_rect)

        # Draw paper #
        pg.draw.circle(self.screen, (255, 255, 255), (self.width_screen/2, self.height_screen/2), self.radius_detail)

        # Draw details #
        self.draw_image()

    def main(self):
        self.build()

        # Clock #
        stp.CLOCK.tick(c.FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
				RUNNING = False

        # Draw screen #
        self.draw_screen()

        # *flip update screen*
        pg.display.flip()

        pg.time.wait(3500)
