#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
from ..components.board import Board
from ..components.player import Player
from detail import DetailText, DetailImage
from button import ButtonText, ButtonImage
from .. import setup as stp
from .. import constants as c

class Gamescreen:
    def __init__(self, background_game, img_player_1, img_player_2, pause_music, mute_music, resolution_screen, volume_music):
        # Set resolution screen #
        pg.display.set_icon(stp.ICON['kenney_icon'])
        self.screen = pg.display.set_mode(resolution_screen)
        self.resolution_screen = resolution_screen
        self.width_screen = resolution_screen[0]
        self.height_screen = resolution_screen[1]
        # Variables #
        self.background = self.image = pg.transform.scale(stp.BACK['background'], self.resolution_screen)
        self.background_rect = self.background.get_rect()
        self.proporcao = self.width_screen / 1280.0
        self.img_player_1 = img_player_1
        self.img_player_2 = img_player_2
        self.number_divide = (560 * self.proporcao)/8
        # Margins of objects #
        self.margin_game_top = (self.height_screen - int(560 * self.proporcao)) / 2
        self.margin_game_left = int(self.width_screen * 0.05)
        self.margin_buttons_top = int(200 * self.proporcao)
        self.margin_top_kenney = int(71 * self.proporcao)
        self.margin_buttons_music = self.width_screen - (150 * self.proporcao)
        # Size of objects #
        self.size_block_game = (int(560 * self.proporcao), int(560 * self.proporcao))
        self.size_detail_kenney = (int(353 * self.proporcao), int(141 * self.proporcao))
        self.size_back_content_1 = (int(560 * self.proporcao + 40), int(560 * self.proporcao + 40))
        self.size_back_content_2 = (int(300 * self.proporcao), int(150 * self.proporcao))
        self.size_back_content_3 = (int(225 * self.proporcao), int(100 * self.proporcao))
        self.size_details_music = (int(30 * self.proporcao), int(30 * self.proporcao))
        self.size_buttons_music = (int(40 * self.proporcao), int(40 * self.proporcao))
        self.size_button_home = (int(50 * self.proporcao), int(50 * self.proporcao))
        self.size_details_info = (int(300 * self.proporcao), int(50 * self.proporcao))
        self.size_button_desist_round = (int(225 * self.proporcao), int(50 * self.proporcao))
        # Set block game #
        self.background_game = pg.transform.scale(stp.BOARDS[background_game], self.size_block_game)
        self.background_game_rect = self.background_game.get_rect()
        self.background_game_rect.top = self.margin_game_top
        self.background_game_rect.left = self.margin_game_left
        # Distance of objects #
        self.dist_game_info = int(330 * self.proporcao)
        self.dist_buttons_music = int()
        self.dist_captures = int(80 * self.proporcao)
        self.dist_info_round = int(50 * self.proporcao)
        self.dist_info_capture = int(70 * self.proporcao)
        self.dist_all_info = self.margin_game_left + self.size_block_game[0] + self.dist_game_info
        # Padding of objects #
        self.padding_capture = int(200 * self.proporcao)
        self.padding_capture_value = int(20 * self.proporcao)
        self.padding_round_quit = int(150 * self.proporcao)
        # Fonts #
        self.font_text = stp.FONTS['kenney']
        self.font_size = int(20 * self.proporcao)
        # #
        self.mute_music = mute_music
        self.music_pause = pause_music
        self.volume_music = volume_music
        # Define GroupSprite #
    	self.heros_player_one = pg.sprite.Group()
    	self.heros_player_two = pg.sprite.Group()
    	self.hero_move = pg.sprite.Group()
        # Group Details and Buttons #
        self.details_priority = pg.sprite.Group()
        self.details_text = pg.sprite.Group()
        self.details_image = pg.sprite.Group()
        self.buttons_text = pg.sprite.Group()
        self.buttons_image = pg.sprite.Group()
        # Placar e Round #
        self.turn_image = stp.NUMBERS['1']
        self.turn_image_rect = self.turn_image.get_rect()
        self.turn_image_rect.center = (self.dist_all_info + self.padding_round_quit, self.height_screen/2 + 10)
        self.capture_player_one = stp.NUMBERS['0']
        self.capture_player_one_rect = self.capture_player_one.get_rect()
        self.capture_player_one_rect.center = (self.dist_all_info - self.dist_captures, self.height_screen/2 + self.padding_capture + self.padding_capture_value)
        self.capture_player_two = stp.NUMBERS['0']
        self.capture_player_two_rect = self.capture_player_two.get_rect()
        self.capture_player_two_rect.center = (self.dist_all_info + self.dist_captures, self.height_screen/2 + self.padding_capture + self.padding_capture_value)
        # Radius healding Kenney #
        if self.proporcao == 1:
            self.radius_detail = 450
        else:
            self.radius_detail = 415

    def coord(self, coord_pixels):
        return [(coord_pixels[0] - self.margin_game_left)/int(self.number_divide), (coord_pixels[1] - self.margin_game_top)/int(self.number_divide)]

    def verify_click_game(self, pos):
        cpx = pos[0]
        cpy = pos[1]
        if (cpx >= self.margin_game_left and cpx <= self.size_block_game[0] + self.margin_game_left) and (cpy >= self.margin_game_top and cpy <= self.size_block_game[1] + self.margin_game_top):
            return True
        else:
            return False

    def build(self):
        # Details #
        kenney_logo = DetailImage(stp.BACK['paperwhite'], (self.dist_all_info, self.margin_top_kenney), (0, 0), stp.BACK['kenney'], 'kenney', self.size_detail_kenney)
        background_game = DetailText(stp.BACK['backcontent'], (self.margin_game_left + self.size_block_game[0]/2, self.height_screen/2), self.size_back_content_1, '', c.WHITE_COLOR)
        background_info_round = DetailText(stp.BACK['backcontent'], (self.dist_all_info + self.padding_round_quit, self.height_screen/2), self.size_back_content_3, '', c.WHITE_COLOR)
        background_info_capture = DetailText(stp.BACK['backcontent'], (self.dist_all_info, self.height_screen/2 + self.padding_capture), self.size_back_content_2, '', c.WHITE_COLOR)
        text_1 = DetailText(stp.BUTTONS['yellow'], (self.dist_all_info + self.padding_round_quit, self.height_screen/2 - self.dist_info_round), self.size_button_desist_round, 'Vez do jogador', c.BLACK_COLOR)
        text_2 = DetailText(stp.BUTTONS['yellow'], (self.dist_all_info, self.height_screen/2 + self.padding_capture - self.dist_info_capture), self.size_details_info, 'Capturas', c.BLACK_COLOR)
        text_3 = DetailText(stp.BACK['backcontent'], (self.dist_all_info - self.dist_captures, self.height_screen/2 + self.padding_capture - self.padding_capture_value), (0,0), 'Jogador 1', c.BLACK_COLOR)
        text_4 = DetailText(stp.BACK['backcontent'], (self.dist_all_info + self.dist_captures, self.height_screen/2 + self.padding_capture - self.padding_capture_value), (0,0), 'Jogador 2', c.BLACK_COLOR)
        text_5 = DetailText(stp.BUTTONS['yellow'], (self.dist_all_info - self.padding_round_quit, self.height_screen/2 - self.dist_info_round), self.size_button_desist_round, 'Desistir?', c.BLACK_COLOR)

        # Add details in Group #
        self.details_image.add(kenney_logo)
        self.details_priority.add(background_game)
        self.details_priority.add(background_info_round)
        self.details_priority.add(background_info_capture)
        self.details_text.add(text_1)
        self.details_text.add(text_2)
        self.details_text.add(text_3)
        self.details_text.add(text_4)
        self.details_text.add(text_5)

        # Buttons #
        button_home = ButtonImage(1, stp.BUTTONS['blue_circle'], (self.dist_all_info - self.size_buttons_music[0] - self.size_button_home[0]/2, self.margin_buttons_top), self.size_button_home, stp.BUTTONS['home'], 'home', self.size_details_music)
        button_desist = ButtonText(2, stp.BUTTONS['blue'], (self.dist_all_info - self.padding_round_quit, self.height_screen/2 - self.dist_info_round + self.size_button_desist_round[1]), self.size_button_desist_round, 'Sim', c.WHITE_COLOR)
        if self.mute_music:
            button_music_on_off = ButtonImage(3, stp.BUTTONS['blue_circle'], (self.dist_all_info - self.size_buttons_music[0]/2, self.margin_buttons_top), self.size_buttons_music, stp.BUTTONS['music_off'], 'music_off', self.size_details_music)
        else:
            button_music_on_off = ButtonImage(3, stp.BUTTONS['blue_circle'], (self.dist_all_info - self.size_buttons_music[0]/2, self.margin_buttons_top), self.size_buttons_music, stp.BUTTONS['music_on'], 'music_on', self.size_details_music)
        if self.music_pause:
            button_music_pause = ButtonImage(4, stp.BUTTONS['blue_circle'], (self.dist_all_info + self.size_buttons_music[0]/2, self.margin_buttons_top), self.size_buttons_music, stp.BUTTONS['play'], 'play', self.size_details_music)
        else:
            button_music_pause = ButtonImage(4, stp.BUTTONS['blue_circle'], (self.dist_all_info + self.size_buttons_music[0]/2, self.margin_buttons_top), self.size_buttons_music, stp.BUTTONS['pause'], 'pause', self.size_details_music)
        button_music_restart = ButtonImage(5, stp.BUTTONS['blue_circle'], (self.dist_all_info + self.size_buttons_music[0] + self.size_buttons_music[0]/2, self.margin_buttons_top), self.size_buttons_music, stp.BUTTONS['restart'], 'restart', self.size_details_music)

        # Add buttons in Group #
        self.buttons_image.add(button_home)
        self.buttons_image.add(button_music_on_off)
        self.buttons_image.add(button_music_pause)
        self.buttons_image.add(button_music_restart)
        self.buttons_text.add(button_desist)

    def draw_image(self):
        for detail in self.details_image:
            detail.draw_image(self.screen)

        for button in self.buttons_image:
            button.draw_image(self.screen)

    def draw_text(self):
        for detail in self.details_text:
            detail.draw_text(self.screen, self.font_size, self.font_text)

        for button in self.buttons_text:
            button.draw_text(self.screen, self.font_size, self.font_text)

    def draw_screen(self):
        # Update screen #
        self.screen.fill(c.BLACK_COLOR)
        self.screen.blit(self.background, self.background_rect)
        # Draw Details #
        pg.draw.circle(self.screen, (255, 255, 255), (self.dist_all_info, -275), self.radius_detail)
        self.details_priority.draw(self.screen)
        self.details_text.draw(self.screen)
        self.details_image.draw(self.screen)
        self.buttons_image.draw(self.screen)
        self.buttons_text.draw(self.screen)
        # Draw Game Details #
        self.screen.blit(self.background_game, self.background_game_rect)
        self.heros_player_one.draw(self.screen)
        self.heros_player_two.draw(self.screen)
        self.hero_move.draw(self.screen)
        # Draw Details and buttons#
        self.draw_image()
        self.draw_text()
        # Draw Turn and Captures #
        self.screen.blit(self.turn_image, self.turn_image_rect)
        self.screen.blit(self.capture_player_one, self.capture_player_one_rect)
        self.screen.blit(self.capture_player_two, self.capture_player_two_rect)
        # Update Game Hero #
        self.heros_player_one.update()
        self.heros_player_two.update()

    def option(self, pos):
        for button in self.buttons_image:
            if button.click(pos):
                id_button = button.get_id()
                if id_button == 3:
                    if self.mute_music:
                        self.mute_music = False
                        button.set_image(stp.BUTTONS['music_on'])
                    else:
                        self.mute_music = True
                        button.set_image(stp.BUTTONS['music_off'])
                elif id_button == 4:
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
        # Initialize game #
    	PLAYER_ONE = Player(self.img_player_1, c.LOCAL_SPRITES_1, 1, (self.margin_game_left, self.margin_game_top), self.number_divide)
    	PLAYER_TWO = Player(self.img_player_2, c.LOCAL_SPRITES_2, 2, (self.margin_game_left, self.margin_game_top), self.number_divide)
    	BOARD = Board(PLAYER_ONE, PLAYER_TWO)
        self.heros_player_one = PLAYER_ONE.get_heros()
    	self.heros_player_two = PLAYER_TWO.get_heros()

        # Building details e outhers #
        self.build()

        # Path music #
        PATH_MUSIC = 'resources/sound/music_game.mp3'

    	# Control Variables #
    	RUNNING = True
    	TURN = 1
        FINISH = 0

        while RUNNING:
            # Clock #
            stp.CLOCK.tick(c.FPS)

            # Check event in game #
            for event in pg.event.get():
            	if event.type == pg.QUIT:
            		RUNNING = False
            	elif event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if self.verify_click_game(pos):
                        BOARD.check_capture_required(TURN)
                        self.hero_move = BOARD.play(self.coord(pos), TURN)
                    OPC = self.option(pos)
                    if OPC == 1:
                        return (0, '', (self.mute_music, self.music_pause))
                    else:
                        if OPC == 2:
                            if TURN == 1:
                                FINISH = 2
                            else:
                                FINISH = 1
                        if OPC == 3:
                            if self.mute_music:
                                pg.mixer.music.set_volume(0.0)
                            else:
                                pg.mixer.music.set_volume(self.volume_music)
                        elif OPC == 4:
                            if self.music_pause:
                                pg.mixer.music.pause()
                            else:
                                pg.mixer.music.unpause()
                        elif OPC == 5:
                            pg.mixer.music.load(PATH_MUSIC)
                            pg.mixer.music.play(30, 3)
                            self.enable_music()
                            self.music_pause = False

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return (0, '', (self.mute_music, self.music_pause))

            # Update all heros #
            BOARD.update_all_heros()
            if not PLAYER_ONE.hero_moving() and TURN == 2:
                PLAYER_ONE.change_type_heros()
            if not PLAYER_TWO.hero_moving() and TURN == 1:
                PLAYER_TWO.change_type_heros()

            # Update placar #
            self.capture_player_one = stp.NUMBERS[str(12 - len(self.heros_player_two))]
            self.capture_player_two = stp.NUMBERS[str(12 - len(self.heros_player_one))]

            # Check Collide #
            BOARD.analisy_capture(TURN, self.heros_player_one, self.heros_player_two)
            self.draw_screen()

            # Check final game #
            if FINISH:
                color_hero = BOARD.get_color_hero(FINISH)
                return (FINISH, color_hero, (self.mute_music, self.music_pause))
            FINISH = BOARD.check_final_game()

            # Flip turn #
            if not BOARD.get_playing():
                TURN = BOARD.check_flip_turn(TURN)
            self.turn_image = stp.NUMBERS[str(TURN)]

            pg.display.flip()
        pg.quit()
