#coding: utf-8
__author__ = 'thiagowhispher'

import pygame as pg
import constants as c
import setup as stp
from states.openingscreen import Openingscreen
from states.mainscreen import Mainscreen
from states.gamescreen import Gamescreen
from states.configscreen import Configscreen
from states.stylescreen import Stylescreen
from states.winnerscreen import Winnerscreen

def save_resolution(new_resolution):
	clear_file = open(c.PATH_FILE_RESOLUTION, 'w').close()
	file_resolution = open(c.PATH_FILE_RESOLUTION, 'w')
	new_resolution = str(new_resolution[0]) + ' ' + str(new_resolution[1])
	file_resolution.write(new_resolution)
	file_resolution.close()

def main():
	background = 'map_1'
	img_player_1 = 'yellow_hero'
	img_player_2 = 'blue_hero'

	resolution_screen = c.SIZE_SCREEN
	volume_music = 1.0
	mute_music = False
	pause_music = False

	pg.mixer.music.load('resources/sound/music_game.mp3')
	pg.mixer.music.play(30)
	pg.mixer.music.set_volume(volume_music)

	screen = Openingscreen(resolution_screen)
	screen.main()

	pg.time.wait(1000)

	while True:
		screen = Mainscreen(resolution_screen, mute_music, pause_music, volume_music)
		opc, conf = screen.main()
		mute_music, pause_music = conf
		if opc == 1:
			while True:
				stp.open_back(True)
				screen = Gamescreen(background, img_player_1, img_player_2, pause_music, mute_music, resolution_screen, volume_music)
				winner, color_hero, conf = screen.main()
				mute_music, pause_music = conf
				if winner:
					stp.open_back(True)
					screen = Winnerscreen(winner, color_hero, resolution_screen)
					opc = screen.main()
					if opc == 2:
						stp.open_back(False)
						break
				else:
					stp.open_back(False)
					break
		elif opc == 2:
			stp.open_back(True)
			screen = Stylescreen(background, img_player_1, img_player_2, resolution_screen)
			save_or_no, styles = screen.main()
			stp.open_back(False)
			if save_or_no:
				background, img_player_1, img_player_2 = styles
		elif opc == 3:
			stp.open_back(True)
			screen = Configscreen(mute_music, volume_music, resolution_screen)
			save_or_no, conf = screen.main()
			stp.open_back(False)
			if save_or_no:
				mute_music, volume_music, resolution_screen = conf
		else:
			break

	save_resolution(resolution_screen)
	pg.quit()
