import sys
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        '''初始化游戏进程'''
        pygame.init()
        # 加载设置类
        self.settings = Settings()
        # 设置一个像素(1200,800)的屏幕
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
        self.settings.screen_height))    
        # 全屏
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width =  self.screen.get_rect().width
        # self.settings.screen_height =  self.screen.get_rect().height
        # 设置标题
        pygame.display.set_caption("Alient Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        '''开始游戏主循环'''
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullet()
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
        elif event.key == pygame.K_UP:
            self.ship.move_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_event_keyup(self, event):
        # 停止移动
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_UP:  
            self.ship.move_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False  

    def _fire_bullet(self):
        '''创建一颗子弹，放入编组中'''
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _update_bullet(self):
        # 调用编组中每个bullet的update
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0 :
                self.bullets.remove(bullet)
        # print(len(self.bullets)) 

    def __update_screen(self):
        '''每次循环都重绘屏幕'''
        self.screen.fill(self.settings.bg_color)
        # 加载飞船
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _create_fleet(self):
        '''创建外星人群'''
        alien = Alien(self)
        alien_width = alien.rect.width

        available_screen_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_screen_x // (2* alien_width)

        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width +  2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)


        self.aliens.add(alien)

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
