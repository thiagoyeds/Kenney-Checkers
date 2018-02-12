#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
from button import ButtonText, ButtonImage
from detail import DetailImage, DetailText
from .. import setup as stp
from .. import constants as c

class Configscreen:
    def __init__(self, mute_music, volume_music, resolution_screen):
        # Set resolution screen #
        pg.display.set_icon(stp.ICON['kenney_icon'])
        self.screen = pg.display.set_mode(resolution_screen)
        self.resolution_screen = resolution_screen
        self.width_screen = resolution_screen[0]
        self.height_screen = resolution_screen[1]
        # Configuration Game #
        self.mute_music = mute_music
        self.volume_music = volume_music
        self.volume = int(volume_music * 100)
        # Create group buttons
        self.buttons_text = pg.sprite.Group()
        self.buttons_image = pg.sprite.Group()
        self.details_image = pg.sprite.Group()
        self.details_text = pg.sprite.Group()
        # Variables #
        self.proporcao = self.width_screen / 1280.0
        self.background = pg.transform.scale(stp.BACK['background'], self.resolution_screen)
        self.background_rect = self.background.get_rect()
        # Size of objects #
        self.size_buttons = (int(250 * self.proporcao), int(60 * self.proporcao))
        self.size_buttons_check = (int(50 * self.proporcao), int(50 * self.proporcao))
        self.size_detail_kenney = (int(353 * self.proporcao), int(141 * self.proporcao))
        self.size_button_save = (int(353 * self.proporcao), int(51 * self.proporcao))
        self.size_volume_info = (int(100 * self.proporcao), int(50 * self.proporcao))
        # Distance of objects #
        self.dist_object = int(20 * self.proporcao)
        # Margins of objects #
        self.margin_top_kenney = int(71 * self.proporcao)
        self.margin_top = self.height_screen/2 + int(50 * self.proporcao)
        self.margin_bottom = int(75 * self.proporcao)
        # Fonts #
        self.font_button = int(20 * self.proporcao)
        self.font_text = stp.FONTS['kenney']
        # Radius healding Kenney #
        if self.proporcao == 1:
            self.radius_detail = 450
        else:
            self.radius_detail = 415

    def apply_new_resolution(self):
        # Variables #
        self.background = pg.transform.scale(stp.BACK['background'], self.resolution_screen)
        self.background_rect = self.background.get_rect()
        self.proporcao = self.width_screen / 1280.0
        # Size of objects #
        self.size_buttons = (int(250 * self.proporcao), int(60 * self.proporcao))
        self.size_buttons_check = (int(50 * self.proporcao), int(50 * self.proporcao))
        self.size_detail_kenney = (int(353 * self.proporcao), int(141 * self.proporcao))
        self.size_button_save = (int(353 * self.proporcao), int(51 * self.proporcao))
        # Distance of objects #
        self.dist_object = int(20 * self.proporcao)
        # Margins of objects #
        self.margin_top_kenney = int(71 * self.proporcao)
        self.margin_top = self.height_screen/2 + int(50 * self.proporcao)
        self.margin_bottom = int(75 * self.proporcao)
        self.size_volume_info = (int(100 * self.proporcao), int(50 * self.proporcao))
        # Fonts #
        self.font_button = int(20 * self.proporcao)
        self.font_text = stp.FONTS['kenney']
        # Radius healding Kenney #
        if self.proporcao == 1:
            self.radius_detail = 450
        else:
            self.radius_detail = 415

    def build(self):
        # Details #
        kenney_logo = DetailImage(stp.BACK['paperwhite'], (self.width_screen/2, self.margin_top_kenney), (0, 0), stp.BACK['kenney'], 'kenney', self.size_detail_kenney)
        detail_resolution = DetailText(stp.BUTTONS['yellow'], (self.width_screen/2 - self.size_buttons[0] - self.dist_object, self.margin_top - self.size_buttons[1] - self.dist_object), self.size_buttons, 'Resolucao', c.BLACK_COLOR)
        detail_volume = DetailText(stp.BUTTONS['yellow'], (self.width_screen/2 - self.size_buttons[0] - self.dist_object, self.margin_top), self.size_buttons, 'Volume', c.BLACK_COLOR)
        detail_mute = DetailText(stp.BUTTONS['yellow'], (self.width_screen/2 - self.size_buttons[0] - self.dist_object, self.margin_top + self.size_buttons[1] + self.dist_object), self.size_buttons, 'Mute', c.BLACK_COLOR)
        self.detail_volume_info = DetailText(stp.BUTTONS['blue_board'], (self.width_screen/2, self.margin_top), self.size_volume_info, str(self.volume)+'%', c.BLACK_COLOR)

        # Add details in Group #
        self.details_image.empty()
       	self.details_image.add(kenney_logo)
        self.details_text.empty()
        self.details_text.add(detail_resolution)
        self.details_text.add(detail_volume)
        self.details_text.add(detail_mute)
        self.details_text.add(self.detail_volume_info)

        # Buttons #
        button_resolution_1 = ButtonText(1, stp.BUTTONS['blue_board'], (self.width_screen/2, self.margin_top - self.size_buttons[1] - self.dist_object), self.size_buttons, '1280 x 720', c.BLACK_COLOR)
        button_resolution_2 = ButtonText(1, stp.BUTTONS['blue_board'], (self.width_screen/2 + self.size_buttons[0] + self.dist_object, self.margin_top - self.size_buttons[1] - self.dist_object), self.size_buttons, '1024 x 576', c.BLACK_COLOR)
        button_volume_1 = ButtonText(2, stp.BUTTONS['blue_circle'], (self.width_screen/2 - self.size_buttons[0]/4 - self.dist_object, self.margin_top), self.size_buttons_check, '-', c.WHITE_COLOR)
        button_volume_2 = ButtonText(2, stp.BUTTONS['blue_circle'], (self.width_screen/2 + self.size_buttons[0]/4 + self.dist_object, self.margin_top), self.size_buttons_check, '+', c.WHITE_COLOR)
        button_mute_1 = ButtonImage(3, stp.BUTTONS['blue_board_block'], (self.width_screen/2 - self.size_buttons_check[0] - self.dist_object, self.margin_top + self.size_buttons[1] + self.dist_object), self.size_buttons_check, stp.BUTTONS['white_check'], 'check', (self.size_buttons_check[0] - 30, self.size_buttons_check[1] - 30))
        button_mute_2 = ButtonImage(3, stp.BUTTONS['blue_board_block'], (self.width_screen/2 + self.size_buttons_check[0] + self.dist_object, self.margin_top + self.size_buttons[1] + self.dist_object), self.size_buttons_check, stp.BUTTONS['white_cross'], 'cross', (self.size_buttons_check[0] - 30, self.size_buttons_check[1] - 30))
        button_save = ButtonText(4, stp.BUTTONS['blue'], (self.width_screen/2, self.height_screen - self.margin_bottom), self.size_button_save, 'Salvar e voltar', c.WHITE_COLOR)

        if map(int, button_resolution_1.get_text().split(' x ')) == self.resolution_screen:
            button_resolution_1.set_image(stp.BUTTONS['blue'])
            button_resolution_1.set_color_text(c.WHITE_COLOR)
        else:
            button_resolution_2.set_image(stp.BUTTONS['blue'])
            button_resolution_2.set_color_text(c.WHITE_COLOR)

        if self.mute_music:
            button_mute_1.up_lower_button(True)
            button_mute_1.set_image(stp.BUTTONS['blue_check'])
        else:
            button_mute_2.up_lower_button(True)
            button_mute_2.set_image(stp.BUTTONS['blue_cross'])

        button_mute_1.set_up(5)
        button_mute_2.set_up(5)

        # Add Buttons in Group #
        self.buttons_text.empty()
        self.buttons_text.add(button_resolution_1)
        self.buttons_text.add(button_resolution_2)
        self.buttons_text.add(button_volume_1)
        self.buttons_text.add(button_volume_2)
        self.buttons_text.add(button_save)
        self.buttons_image.empty()
        self.buttons_image.add(button_mute_1)
        self.buttons_image.add(button_mute_2)


    def draw_text(self):
        for button in self.buttons_text:
            button.draw_text(self.screen, self.font_button, self.font_text)

        for detail in self.details_text:
        	detail.draw_text(self.screen, self.font_button, self.font_text)

    def draw_image(self):
    	for detail in self.details_image:
    		detail.draw_image(self.screen)

        for button in self.buttons_image:
            button.draw_image(self.screen)

    def draw_screen(self):
        self.screen.fill(c.GREEN_COLOR)
        self.screen.blit(self.background, self.background_rect)

        # Draw paper for buttons #
        pg.draw.circle(self.screen, (255, 255, 255), (self.width_screen / 2, -275), self.radius_detail)

        # Draw buttons #
        self.buttons_text.draw(self.screen)
        self.buttons_image.draw(self.screen)

        # Draw details #
        self.details_text.draw(self.screen)

        # Draw texts and images #
       	self.draw_image()
        self.draw_text()

    def disable_button(self, id_button):
        for button in self.buttons_text:
            if button.get_id() == id_button:
                if id_button == 1:
                    button.set_image(stp.BUTTONS['blue_board'])
                    id_button = button .get_id()

            for button in self.buttons_image:
                if button.get_id() == id_button:
                    if id_button == 3:
                        ckeck_or_cross = button.get_img()
                        button.set_image(stp.BUTTONS['white_'+ckeck_or_cross])
                        button.up_lower_button(False)

    def option(self, pos):
        for button in self.buttons_text:
            if button.click(pos):
                id_button = button.get_id()
                if id_button == 1:
                    self.disable_button(id_button)
                    button.set_image(stp.BUTTONS['blue'])
                    return (id_button, button.get_text())
                elif id_button == 2:
                    action = button.get_text()
                    if self.volume >= 10 and action == '-':
                        self.volume -= 10
                    elif self.volume <= 90 and action == '+':
                        self.volume += 10
                    self.volume_music = self.volume / 100.0
                    self.detail_volume_info.set_text(str(self.volume)+'%')
                    pg.mixer.music.set_volume(self.volume_music)
                elif id_button == 4:
                    return (4, '')


        for button in self.buttons_image:
            if button.click(pos):
                id_button = button.get_id()
                self.disable_button(id_button)
                check_or_cross = button.get_img()
                button.set_image(stp.BUTTONS['blue_'+check_or_cross])
                button.up_lower_button(True)
                if check_or_cross == 'check':
                    check_or_cross = True
                else:
                    check_or_cross = False
                return (id_button, check_or_cross)

        return (0, '')

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
                    opc, action = self.option(pg.mouse.get_pos())
                    if opc == 1:
                        self.resolution_screen = map(int, action.split(' x '))
                        self.screen = pg.display.set_mode(self.resolution_screen)
                        self.width_screen = self.resolution_screen[0]
                        self.height_screen = self.resolution_screen[1]
                        self.apply_new_resolution()
                        self.build()
                    elif opc == 3:
                        self.mute_music = action
                        if action:
                            pg.mixer.music.set_volume(0.0)
                        else:
                            pg.mixer.music.set_volume(self.volume_music)
                    elif opc == 4:
                        return [True, (self.mute_music, self.volume_music, self.resolution_screen)]
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return [False, ()]

            # Draw screen #
            self.draw_screen()

            # *flip update screen*
            pg.display.flip()
        pg.quit()
