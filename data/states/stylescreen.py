#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
from button import ButtonText, ButtonImage
from detail import DetailText, DetailImage
from .. import setup as stp
from .. import constants as c

class Stylescreen:
    def __init__(self, background_game, img_player_1, img_player_2, resolution_screen):
        # Set resolution screen #
        self.screen = pg.display.set_mode(resolution_screen)
        self.resolution_screen = resolution_screen
        self.width_screen = resolution_screen[0]
        self.height_screen = resolution_screen[1]
        # Style game #
        self.background_game = background_game
        self.img_player_1 = img_player_1
        self.img_player_2 = img_player_2
        self.upper_buttons = (self.background_game, self.img_player_1, self.img_player_2)
        # Create group buttons #
        self.buttons_text = pg.sprite.Group()
        self.buttons_image = pg.sprite.Group()
        self.details_text = pg.sprite.Group()
        self.details_image = pg.sprite.Group()
        self.details = pg.sprite.Group()
        # Variables #
        self.background = pg.transform.scale(stp.BACK['background'], c.SIZE_SCREEN)
        self.background_rect = self.background.get_rect()
        self.proporcao = self.width_screen / 1280.0
        # Size of objects #
        self.size_detail_kenney = (int(353 * self.proporcao), int(141 * self.proporcao))
        self.size_back_buttons = (int(100 * self.proporcao), int(100 * self.proporcao))
        self.size_back_content_1 = (int(400 * self.proporcao), int(300 * self.proporcao))
        self.size_back_content_2 = (int(300 * self.proporcao), int(300 * self.proporcao))
        self.size_buttons = (int(250 * self.proporcao), int(50 * self.proporcao))
        self.size_button_save = (int(353 * self.proporcao), int(51 * self.proporcao))
        self.size_details_buttons = (int(40 * self.proporcao), int(60 * self.proporcao))
        # Padding of objects #
        self.padding_boards_1 = self.width_screen/4
        self.padding_boards_2 = int(350 * self.proporcao)
        # Margins of objects #
        self.margin_buttons_left = int(60 * self.proporcao)
        self.margin_buttons_top = self.height_screen/2 - int(100 * self.proporcao)
        self.margin_bottom = int(75 * self.proporcao)
        self.margin_top_kenney = int(71 * self.proporcao)
        self.margin_board_1 = self.width_screen/2 - self.width_screen/4
        self.margin_board_2 = self.margin_board_1 + self.size_back_content_1[0]/2 + self.size_back_content_2[0]/2 + 10
        self.margin_board_3 = self.margin_board_2 + self.size_back_content_2[0] + 10
        # Distance of buttons #
        self.dist_button_board = int(150 * self.proporcao)
        self.dist_buttons = int(20 * self.proporcao)
        self.dist_position_buttons = int(100 * self.proporcao)
        # Fonts #
        self.font_button = int(20 * self.proporcao)
        self.font_text = stp.FONTS['kenney']
        # Radius healding Kenney #
        if self.proporcao == 1:
            self.radius_detail = 450
        else:
            self.radius_detail = 415

    def up_button(self):
        for button in self.buttons_image:
            if button.get_img() in self.upper_buttons:
                button.up_lower_button(True)
    def build(self):
        # Details #
        kenney_logo = DetailImage(stp.BACK['paperwhite'], (self.width_screen/2, self.margin_top_kenney), (0, 0), stp.BACK['kenney'], 'kenney', self.size_detail_kenney)
        boards_div = DetailText(stp.BUTTONS['yellow'], (self.margin_board_1, self.margin_buttons_top), self.size_buttons, 'Tabuleiro', c.BLACK_COLOR)
        player1_div = DetailText(stp.BUTTONS['yellow'], (self.margin_board_2, self.margin_buttons_top), self.size_buttons, 'Player 1', c.BLACK_COLOR)
        player2_div = DetailText(stp.BUTTONS['yellow'], (self.margin_board_3, self.margin_buttons_top), self.size_buttons, 'Player 2', c.BLACK_COLOR)
        background_boards = DetailText(stp.BACK['backcontent'], (self.margin_board_1, self.margin_buttons_top + self.dist_button_board), self.size_back_content_1, '', c.BLACK_COLOR)
        background_player1 = DetailText(stp.BACK['backcontent'], (self.margin_board_2, self.margin_buttons_top + self.dist_button_board), self.size_back_content_2, '', c.BLACK_COLOR)
        background_player2 = DetailText(stp.BACK['backcontent'], (self.margin_board_3, self.margin_buttons_top + self.dist_button_board), self.size_back_content_2, '', c.BLACK_COLOR)

        # Add details in Group #
        self.details_image.add(kenney_logo)
        self.details_text.add(boards_div)
        self.details_text.add(player1_div)
        self.details_text.add(player2_div)

        # Add details in Group
        self.details.add(background_boards)
        self.details.add(background_player1)
        self.details.add(background_player2)

        # Buttons #
        button_map_1 = ButtonImage(1, stp.BACK['paperwhite'], (self.margin_board_1 - self.size_back_content_1[0]/4, self.margin_buttons_top + self.dist_position_buttons), self.size_back_buttons, stp.BOARDS['map_1'], 'map_1', (self.size_back_buttons[0] - 10, self.size_back_buttons[1] - 10))
        button_map_2 = ButtonImage(1, stp.BACK['paperwhite'], (self.margin_board_1 + self.size_back_content_1[0]/4, self.margin_buttons_top + self.dist_position_buttons), self.size_back_buttons, stp.BOARDS['map_2'], 'map_2', (self.size_back_buttons[0] - 10, self.size_back_buttons[1] - 10))
        button_map_3 = ButtonImage(1, stp.BACK['paperwhite'], (self.margin_board_1 - self.size_back_content_1[0]/4, self.margin_buttons_top + self.dist_position_buttons + self.size_back_buttons[0] + self.dist_buttons), self.size_back_buttons, stp.BOARDS['map_3'], 'map_3', (self.size_back_buttons[0] - 10, self.size_back_buttons[1] - 10))
        button_map_4 = ButtonImage(1, stp.BACK['paperwhite'], (self.margin_board_1 + self.size_back_content_1[0]/4, self.margin_buttons_top + self.dist_position_buttons + self.size_back_buttons[0] + self.dist_buttons), self.size_back_buttons, stp.BOARDS['map_4'], 'map_4', (self.size_back_buttons[0] - 10, self.size_back_buttons[1] - 10))

        button_green = ButtonImage(2, stp.BACK['paperwhite'], (self.margin_board_2 , self.margin_buttons_top + self.dist_position_buttons), self.size_back_buttons, stp.HEROS['green_hero'], 'green_hero', self.size_details_buttons)
        button_yellow = ButtonImage(2, stp.BACK['paperwhite'], (self.margin_board_2, self.margin_buttons_top + self.dist_position_buttons + self.size_back_buttons[0] + self.dist_buttons), self.size_back_buttons, stp.HEROS['yellow_hero'], 'yellow_hero', self.size_details_buttons)

        button_blue = ButtonImage(3, stp.BACK['paperwhite'], (self.margin_board_3, self.margin_buttons_top + self.dist_position_buttons), self.size_back_buttons, stp.HEROS['blue_hero'], 'blue_hero', self.size_details_buttons)
        button_pink = ButtonImage(3, stp.BACK['paperwhite'], (self.margin_board_3, self.margin_buttons_top + self.dist_position_buttons + self.size_back_buttons[0] + self.dist_buttons), self.size_back_buttons, stp.HEROS['pink_hero'], 'pink_hero',self.size_details_buttons)

        button_save = ButtonText(4, stp.BUTTONS['blue'], (self.width_screen/2, self.height_screen - self.margin_bottom), self.size_button_save, 'Salvar e voltar', c.WHITE_COLOR)

        # Add Buttons in Group #
        self.buttons_image.add(button_map_1)
        self.buttons_image.add(button_map_2)
        self.buttons_image.add(button_map_3)
        self.buttons_image.add(button_map_4)

        self.buttons_image.add(button_green)
        self.buttons_image.add(button_yellow)

        self.buttons_image.add(button_blue)
        self.buttons_image.add(button_pink)

        self.buttons_text.add(button_save)

        self.up_button()

    def draw_text(self):
        for button in self.buttons_text:
            button.draw_text(stp.SCREEN, self.font_button, self.font_text)

        for detail in self.details_text:
            detail.draw_text(stp.SCREEN, self.font_button, self.font_text)

    def draw_image(self):
        for detail in self.details_image:
            detail.draw_image(stp.SCREEN)

        for button in self.buttons_image:
            button.draw_image(stp.SCREEN)

    def draw_screen(self):
        stp.SCREEN.fill(c.GREEN_COLOR)
        stp.SCREEN.blit(self.background, self.background_rect)

        # Draw paper #
        pg.draw.circle(stp.SCREEN, (255, 255, 255), (self.width_screen / 2, -275), self.radius_detail)
        self.details.draw(stp.SCREEN)

        # Draw details #
        self.details_text.draw(stp.SCREEN)
        self.details_image.draw(stp.SCREEN)

        # Draw buttons #
        self.buttons_text.draw(stp.SCREEN)
        self.buttons_image.draw(stp.SCREEN)

        # Texts e images#
        self.draw_image()
        self.draw_text()

    def disable_button(self, id_button):
        for button in self.buttons_image:
            if button.get_id() == id_button:
                button.up_lower_button(False)

    def option(self, pos):
        for button in self.buttons_image:
            if button.click(pos):
                result = (button.get_id() ,button.get_img())
                self.disable_button(result[0])
                button.up_lower_button(True)
                return result

        for button in self.buttons_text:
            if button.click(pos):
                return (button.get_id(), None)

        return (5, None)

    def main(self):
        self.build()

        # Control Variables #
        RUNNING = True

        while RUNNING:
            # Clock #
            stp.CLOCK.tick(c.FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
    				RUNNING = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    id_opt, img = self.option(pg.mouse.get_pos())
                    if id_opt == 1:
                        self.background_game = img
                    elif id_opt == 2:
                        self.img_player_1 = img
                    elif id_opt == 3:
                        self.img_player_2 = img
                    elif id_opt == 4:
                        return (True, (self.background_game, self.img_player_1, self.img_player_2))
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return (False, ())


            # Draw screen #
            self.draw_screen()

            # *flip update screen*
            pg.display.flip()
        pg.quit()
