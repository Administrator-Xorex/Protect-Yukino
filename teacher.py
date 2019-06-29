import pygame
from pygame.sprite import Sprite

class Teacher(Sprite):
    def __init__(self,number,screen):
        super(Teacher,self).__init__()
        self.screen=screen
        self.number=number

        self.image=pygame.image.load('images/teacher.bmp')
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=False:
            return True

    def update(self):
        self.x+=(self.number.teacher_speed_factor*self.number.fleet_direction)
        self.rect.x=self.x
    

        
