#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
from button import ButtonText, ButtonImage
from detail import DetailImage
from .. import setup as stp
from .. import constants as c

class Mainscreen:
    def __init__(self, resolution_screen, mute_music, pause_music, volume_music):
        # Create group buttons
        self.buttons_text = pg.sprite.Group()
        self.buttons_image = pg.sprite.Group()
        self.details_image = pg.sprite.Group()
        # Set resolution screen #
        pg.display.set_icon(stp.ICON['kenney_icon'])
        screen = pg.display.set_mode(resolution_screen)
        self.resolution_screen = resolution_screen
        self.width_screen = resolution_screen[0]
        self.height_screen = resolution_screen[1]

        # Variables #
        self.proporcao = self.width_screen / 1280.0
        self.background = pg.transform.scale(stp.BACK['background'], self.resolution_screen)
        self.background_rect = self.background.get_rect()
        # Size of objects #
        self.size_buttons = (int(300 * self.proporcao), int(60 * self.proporcao))
        self.size_details_buttons = (int(50 * self.proporcao), int(50 * self.proporcao))
        self.size_buttons_music = (int(40 * self.proporcao), int(40 * self.proporcao))
        self.size_details_music = (int(30 * self.proporcao), int(30 * self.proporcao))
        self.size_detail_kenney = (int(353 * self.proporcao), int(141 * self.proporcao))
        self.size_detail_screenshot = (int(500 * self.proporcao), int(300 * self.proporcao))
	self.size_kenney_logo = (int(100 * self.proporcao), int(40 * self.proporcao))
        # Margin of objects #
        self.margin_buttons_music = self.width_screen - (150 * self.proporcao)
        self.margin_top_kenney = int(71 * self.proporcao)
        self.margin_top = self.height_screen/2 + int(50 * self.proporcao)
        self.margin_left = self.width_screen/4
        self.margin_left_screenshot = self.width_screen/2 + self.width_screen/6
        # Padding of screenshots #
        self.padding_screenshot = int(75 * self.proporcao)
        # Distance of buttons #
        self.dist_buttons = int(10 * self.proporcao)
        # Control music #
        self.mute_music = mute_music
        self.music_pause = pause_music
        self.volume_music = volume_music
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
        back_screenshot_1 = DetailImage(stp.BACK['backcontent'], (self.margin_left_screenshot, self.margin_top - self.padding_screenshot), (0, 0), stp.REFERENCES['kenney_site'], 'kenney_site', self.size_detail_screenshot)
        back_screenshot_2 = DetailImage(stp.BACK['backcontent'], (self.margin_left_screenshot, self.margin_top + self.padding_screenshot), (0, 0), stp.REFERENCES['kenney_channel'], 'kenney_channel', self.size_detail_screenshot)
	back_screenshot_3 = DetailImage(stp.BACK['backcontent'], (self.width_screen - self.size_kenney_logo[0]/2 - self.dist_buttons, self.height_screen - self.size_kenney_logo[1]/2 - self.dist_buttons), (0, 0), stp.BACK['kenney_logo'], 'kenney_logo', self.size_kenney_logo)
        detail_play = DetailImage(stp.BACK['paperwhite'], (self.margin_left - (self.size_buttons[0]/2) + 25, self.margin_top - self.size_buttons[1]/2 - self.size_buttons[1] - self.dist_buttons * 2), (0, 0), stp.BUTTONS['play_game'], 'play_game', self.size_details_buttons)
        detail_style = DetailImage(stp.BACK['paperwhite'], (self.margin_left - (self.size_buttons[0]/2) + 25, self.margin_top - self.size_buttons[1]/2 - self.dist_buttons), (0, 0), stp.BUTTONS['style'], 'style', self.size_details_buttons)
        detail_config = DetailImage(stp.BACK['paperwhite'], (self.margin_left - (self.size_buttons[0]/2) + 25, self.margin_top + self.size_buttons[1]/2), (0, 0), stp.BUTTONS['gear'], 'gear', self.size_details_buttons)
        detail_quit = DetailImage(stp.BACK['paperwhite'], (self.margin_left - (self.size_buttons[0]/2) + 25, self.margin_top + self.size_buttons[1]/2 + self.size_buttons[1] + self.dist_buttons), (0, 0), stp.BUTTONS['exit'], 'exit', self.size_details_buttons)

        # Rotate the screenshots #
        back_screenshot_1.rotate(5)
        back_screenshot_2.rotate(15)

        # Add details in Group #
        self.details_image.add(kenney_logo)
        self.details_image.add(detail_play)
        self.details_image.add(detail_style)
        self.details_image.add(detail_config)
        self.details_image.add(detail_quit)
        self.details_image.add(back_screenshot_1)
        self.details_image.add(back_screenshot_2)
	self.details_image.add(back_screenshot_3)

        # Buttons #
        button_start = ButtonText(1, stp.BUTTONS['blue'], (self.margin_left, self.margin_top - self.size_buttons[1]/2 - self.size_buttons[1] - self.dist_buttons * 2), self.size_buttons, 'Jogar', c.WHITE_COLOR)
        button_style = ButtonText(2, stp.BUTTONS['blue'], (self.margin_left, self.margin_top - self.size_buttons[1]/2 - self.dist_buttons), self.size_buttons, 'Estilos', c.WHITE_COLOR)
        button_config = ButtonText(3, stp.BUTTONS['blue'], (self.margin_left, self.margin_top + self.size_buttons[1]/2), self.size_buttons, 'Configuracao', c.WHITE_COLOR)
        button_quit = ButtonText(4, stp.BUTTONS['blue'], (self.margin_left, self.margin_top + self.size_buttons[1]/2 + self.size_buttons[1] + self.dist_buttons), self.size_buttons, 'Sair', c.WHITE_COLOR)
        if self.mute_music:
            button_music_on_off = ButtonImage(5, stp.BUTTONS['blue_circle'], (self.margin_buttons_music - self.size_buttons_music[0] * 2, 40), self.size_buttons_music, stp.BUTTONS['music_off'], 'music_off', self.size_details_music)
        else:
            button_music_on_off = ButtonImage(5, stp.BUTTONS['blue_circle'], (self.margin_buttons_music - self.size_buttons_music[0] * 2, 40), self.size_buttons_music, stp.BUTTONS['music_on'], 'music_on', self.size_details_music)
        if self.music_pause:
            button_music_pause = ButtonImage(6, stp.BUTTONS['blue_circle'], (self.margin_buttons_music - self.size_buttons_music[0] , 40), self.size_buttons_music, stp.BUTTONS['play'], 'play', self.size_details_music)
        else:
            button_music_pause = ButtonImage(6, stp.BUTTONS['blue_circle'], (self.margin_buttons_music - self.size_buttons_music[0] , 40), self.size_buttons_music, stp.BUTTONS['pause'], 'pause', self.size_details_music)
        button_music_restart = ButtonImage(7, stp.BUTTONS['blue_circle'], (self.margin_buttons_music, 40), self.size_buttons_music, stp.BUTTONS['restart'], 'restart', self.size_details_music)

        # Add Buttons in Group #
        self.buttons_text.add(button_start)
        self.buttons_text.add(button_style)
        self.buttons_text.add(button_config)
        self.buttons_text.add(button_quit)
        self.buttons_image.add(button_music_on_off)
        self.buttons_image.add(button_music_pause)
        self.buttons_image.add(button_music_restart)

    def draw_text(self):
        for button in self.buttons_text:
            button.draw_text(stp.SCREEN, self.font_button, self.font_text)

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

        # Draw buttons #
        self.buttons_text.draw(stp.SCREEN)
        self.buttons_image.draw(stp.SCREEN)
        self.draw_text()

        # Draw details #
        self.details_image.draw(stp.SCREEN)
        self.draw_image()

    def option(self, pos):
        for button in self.buttons_image:
            if button.click(pos):
                id_button = button.get_id()
                if id_button == 5:
                    if self.mute_music:
                        self.mute_music = False
                        button.set_image(stp.BUTTONS['music_on'])
                    else:
                        self.mute_music = True
                        button.set_image(stp.BUTTONS['music_off'])
                elif id_button == 6:
                    if self.music_pause:
                        self.music_pause = False
                        button.set_image(stp.BUTTONS['pause'])
                    else:
                        self.music_pause = True
                        button.set_image(stp.BUTTONS['play'])
                return id_button

        for button in self.buttons_text:
            if button.click(pos):
                return button.get_id()
        return 0

    def enable_music(self):
        for button in self.buttons_image:
            id_button = button.get_id()
            if id_button == 6:
                button.set_image(stp.BUTTONS['pause'])


    def main(self):
        self.build()

        # Path music #
        PATH_MUSIC = 'resources/sound/music_game.mp3'

        # Control Variables #
        RUNNING = True

        while RUNNING:
            # Clock #
            stp.CLOCK.tick(c.FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
    				RUNNING = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    opc = self.option(pg.mouse.get_pos())
                    if opc > 0 and opc < 5:
                        return (opc, (self.mute_music, self.music_pause))
                    else:
                        if opc == 5:
                            if self.mute_music:
                                pg.mixer.music.set_volume(0.0)
                            else:
                                pg.mixer.music.set_volume(self.volume_music)
                        elif opc == 6:
                            if self.music_pause:
                                pg.mixer.music.pause()
                            else:
                                pg.mixer.music.unpause()
                        elif opc == 7:
                            pg.mixer.music.load(PATH_MUSIC)
                            pg.mixer.music.play(30, 3.5)
                            self.enable_music()
                            self.music_pause = False

            # Draw screen #
            self.draw_screen()

            # *flip update screen*
            pg.display.flip()
        pg.quit()
