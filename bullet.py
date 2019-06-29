import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,number,screen,yukino):
        super(Bullet,self).__init__()
        self.screen=screen

        self.rect=pygame.Rect(False,False,number.bullet_width,number.bullet_height)
        self.rect.centerx=yukino.rect.centerx
        self.rect.top=yukino.rect.top
        self.y=float(self.rect.y)
        self.color=number.bullet_color
        self.speed_factor=number.bullet_speed_factor

    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

