import pygame
import functions 

from settings import Settings
from yukino import Yukino
from pygame.sprite import Group
from teacher import Teacher
from stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    number=Settings()
    screen=pygame.display.set_mode((number.screen_width,number.screen_height))
    play_button=Button(number,screen,"Play")
    pygame.display.set_caption("Protect Yukino")

    stats=GameStats(number)
    sb=Scoreboard(number,screen,stats)
    yukino=Yukino(number,screen)
    bullets=Group()
    teachers=Group()
    functions.create_fleet(number,screen,yukino,teachers)


    while True:
        functions.check_events(number,screen,stats,sb,play_button,yukino,teachers,bullets)
        if stats.game_active:
            yukino.update()
            functions.update_bullets(number,screen,stats,sb,yukino,teachers,bullets)
            functions.update_teachers(number,screen,stats,sb,yukino,teachers,bullets)
        functions.update_screen(number,screen,stats,sb,yukino,teachers,bullets,play_button)

run_game()

a=input()


