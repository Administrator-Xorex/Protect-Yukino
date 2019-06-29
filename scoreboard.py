import pygame.font

from pygame.sprite import Group
from yukino import Yukino

class Scoreboard():
    def __init__(self,number,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.number=number
        self.stats=stats

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_yukino()
    
    def prep_score(self):
        score_str="{:,}".format(self.stats.score)
        self.score_image=self.font.render(score_str,
        True,self.text_color,self.number.bg_color)

        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.yukino.draw(self.screen)

    def prep_high_score(self):
        high_score_str="{:,}".format(self.stats.high_score)
        self.high_score_image=self.font.render(high_score_str,
        True,self.text_color,self.number.bg_color)

        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top

    def prep_level(self):
        self.level_image=self.font.render(str(self.stats.level),
            True,self.text_color,self.number.bg_color)
        
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10

    def prep_yukino(self):
        self.yukino=Group()
        for yukino_number in range(self.stats.yukino_left):
            yukino=Yukino(self.number,self.screen)
            yukino.rect.x=10+yukino_number*yukino.rect.width
            yukino.rect.y=10
            self.yukino.add(yukino)
