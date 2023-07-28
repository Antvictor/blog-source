import sys
import pygame
from setting import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        '''初始化游戏进程'''
        pygame.init()
        # 加载设置类
        self.settings = Settings()
        # 设置一个像素(1200,800)的屏幕
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
        self.settings.screen_higth))    
        # 设置标题
        pygame.display.set_caption("Alient Invasion")
        self.ship = Ship(self)

    def run_game(self):
        '''开始游戏主循环'''
        while True:
            self._check_event()
            self.ship.update()
            self.__update_screen()

    def _check_event(self):
        '''监听键盘和鼠标操作'''
        for event in pygame.event.get():
            # 监听到键盘按下
            if event.type == pygame.KEYDOWN:
                self._check_event_keydown(event)
            # 监听到键盘弹起
            elif event.type == pygame.KEYUP:
                self._check_event_keyup(event)

            # 监听到退出
            if event.type == pygame.QUIT :
                # 关闭程序
                sys.exit()

    def _check_event_keydown(self, event):
        '''按下方向键则可以移动'''
        # 右键向右移动
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        # 向左移动
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_event_keyup(self, event):
        # 停止移动
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def __update_screen(self):
        '''每次循环都重绘屏幕'''
        self.screen.fill(self.settings.bg_color)
        # 加载飞船
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
