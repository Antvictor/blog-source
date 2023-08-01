import pygame

class Ship:
    def __init__(self, ai_game):
        '''初始化飞船并设置默认位置'''
        self.screen = ai_game.screen
        # 屏幕的坐标
        self.screen_rect = ai_game.screen.get_rect()
        # 获取设置
        self.settings = ai_game.settings

        # 是否移动
        self.move_right = False
        self.move_left = False
        self.move_top = False
        self.move_down = False

        # 加载图片
        self.image = pygame.image.load("images/ship.bmp")
        # 图片的坐标
        self.rect = self.image.get_rect()
        # 每艘新飞船都在屏幕底部的中心
        self.center_ship()

    def blitme(self):
        '''在指定位置绘画飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''修改飞船位置'''
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.move_top and self.rect.top > 0:
            self.y -= self.settings.ship_speed 
        if self.move_down and self.rect.bottom < self.screen_rect.height:
            self.y += self.settings.ship_speed 
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)