import pygame

from pygame.sprite import Sprite

class Yukino(Sprite):
    def __init__(self,number,screen):
        super(Yukino,self).__init__()
        self.screen=screen
        self.number=number

        self.image=pygame.image.load('images/Yukino.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center=float(self.rect.centerx)

        self.moving_right=False
        self.moving_left=False

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.number.yukino_speed_factor
        if self.moving_left and self.rect.left>False:
            self.center-=self.number.yukino_speed_factor
        self.rect.centerx=self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_yukino(self):
        self.center=self.screen_rect.centerx