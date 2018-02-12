#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
from detail import DetailText, DetailImage
from button import ButtonText, ButtonImage
from .. import setup as stp
from .. import constants as c

class Winnerscreen:
    def __init__(self, winner, color_hero, resolution_screen):
        # Set resolution screen #
        pg.display.set_icon(stp.ICON['kenney_icon'])
        self.screen = pg.display.set_mode(resolution_screen)
        self.resolution_screen = resolution_screen
        self.width_screen = resolution_screen[0]
        self.height_screen = resolution_screen[1]
        # Variable #
        self.background = self.image = pg.transform.scale(stp.BACK['background'], self.resolution_screen)
        self.background_rect = self.background.get_rect()
        self.proporcao = self.width_screen / 1280.0
        self.color_hero = color_hero
        self.winner = winner
        self.message_winner = ''
        # Size of objects #
        self.size_block_winner = (int(500 * self.proporcao), int(250 * self.proporcao))
        self.size_button_winner = (int(225 * self.proporcao), int(50 * self.proporcao))
        self.size_detail_kenney = (int(353 * self.proporcao), int(141 * self.proporcao))
        self.size_detail_hero = (int(50 * self.proporcao), int(70 * self.proporcao))
        # Margins of objects#
        self.margin_top_kenney = int(71 * self.proporcao)
        # Padding of objetcs #
        self.padding_buttons_winner = int(125 * self.proporcao)
        self.padding_info_winner = int(50 * self.proporcao)
        self.padding_info_hero = int(60 * self.proporcao)
        self.padding_hero = int(15 * self.proporcao)
        # Fonts #
        self.font_text = stp.FONTS['kenney']
        self.font_size = int(20 * self.proporcao)
        self.font_size_winner = int(30 * self.proporcao)
        # Group Details and Buttons#
        self.details_priority = pg.sprite.Group()
        self.details_text = pg.sprite.Group()
        self.details_image = pg.sprite.Group()
        self.buttons_text = pg.sprite.Group()
        # Radius healding Kenney #
        if self.proporcao == 1:
            self.radius_detail = 450
        else:
            self.radius_detail = 415

    def build(self):
        # Details #
        kenney_logo = DetailImage(stp.BACK['paperwhite'], (self.width_screen/2, self.margin_top_kenney), (0, 0), stp.BACK['kenney'], 'kenney', self.size_detail_kenney)
        back_finish_game = DetailText(stp.BACK['backcontent'], (self.width_screen/2, self.height_screen/2), self.size_block_winner, '', c.WHITE_COLOR)
        text_6 = DetailText(stp.BUTTONS['yellow'], (self.width_screen/2, self.height_screen/2 - self.size_block_winner[1]/2), self.size_button_winner, 'Fim de jogo', c.BLACK_COLOR)
        self.message_winner = DetailText(stp.BUTTONS['yellow'], (self.width_screen/2, self.height_screen/2 - self.size_block_winner[1]/2 + self.padding_info_winner), (0, 0), 'O jogador '+str(self.winner)+' ganhou', c.BLACK_COLOR)
        hero_winner = DetailImage(stp.BACK['paperwhite'], (self.width_screen/2, self.height_screen/2 - self.padding_hero), (0, 0), stp.HEROS[self.color_hero], '', self.size_detail_hero)

        # Add new details in Group#
        self.details_priority.add(back_finish_game)
        self.details_text.add(text_6)
        self.details_image.add(hero_winner)
        self.details_image.add(kenney_logo)

        # Buttons #
        play_again = ButtonText(1, stp.BUTTONS['blue'], (self.width_screen/2 - self.padding_buttons_winner, self.height_screen/2 + self.padding_info_hero), self.size_button_winner, 'Jogar novamente', c.WHITE_COLOR)
        back_home = ButtonText(2, stp.BUTTONS['blue'], (self.width_screen/2 + self.padding_buttons_winner, self.height_screen/2 + self.padding_info_hero), self.size_button_winner, 'Voltar', c.WHITE_COLOR)

        # Add buttons in Group #
        self.buttons_text.add(play_again)
        self.buttons_text.add(back_home)

    def draw_screen(self):
        # Update screen #
        self.screen.fill(c.BLACK_COLOR)
        self.screen.blit(self.background, self.background_rect)
        # Draw Details #
        pg.draw.circle(self.screen, (255, 255, 255), (self.width_screen/2, -275), self.radius_detail)
        # Draw details and buttons #
        self.details_priority.draw(self.screen)
        self.details_text.draw(self.screen)
        self.details_image.draw(self.screen)
        self.buttons_text.draw(self.screen)

        self.draw_text()
        self.draw_image()

    def draw_image(self):
        for detail in self.details_image:
            detail.draw_image(self.screen)


    def draw_text(self):
        for detail in self.details_priority:
            detail.draw_text(self.screen, self.font_size, self.font_text)

        for detail in self.details_text:
            detail.draw_text(self.screen, self.font_size, self.font_text)

        for button in self.buttons_text:
            button.draw_text(self.screen, self.font_size, self.font_text)

    def option(self, pos):
        for button in self.buttons_text:
            if button.click(pos):
                return button.get_id()

    def main(self):
        # Building details e outhers #
        self.build()

        # Variables Control #
        RUNNING = True
        OPC = 2

        while RUNNING:
            for event in pg.event.get():
            	if event.type == pg.QUIT:
            		RUNNING = False
            	elif event.type == pg.MOUSEBUTTONDOWN:
                    OPC = self.option(pg.mouse.get_pos())
                    if OPC == 1 or OPC == 2:
                        return OPC
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return 2

            # Draw details e buttons #
            self.draw_screen()

            # Message winner #
            self.message_winner.draw_text(self.screen, self.font_size_winner, self.font_text)

            pg.display.flip()
