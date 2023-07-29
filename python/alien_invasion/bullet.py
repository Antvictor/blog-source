import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.color = self.settings.bullet_color
        # 绘制一个矩形
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, 
            self.settings.bullet_height)
        # 和飞船的头部在头一位置
        self.rect.midtop = ai_game.ship.rect.midtop
        # 子弹的位置
        self.y = float(self.rect.y)

    def update(self):
        '''向上移动子弹'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)