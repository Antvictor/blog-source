import sys
from time import sleep
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
import random

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
        # 用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        # 飞船实例
        self.ship = Ship(self)
        # 子弹编组
        self.bullets = pygame.sprite.Group()
        # 外星人编组
        self.aliens = pygame.sprite.Group()
        # 创建外星人群
        self._create_fleet()


    def run_game(self):
        '''开始游戏主循环'''
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullet()
            self._update_alien()
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
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 检测是否与外星人发生碰撞
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # 如果外星人全灭则生成新的外星人群
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

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
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        # 计算可以有多少行
        available_screen_y = (self.settings.screen_height - 
            (3 * alien_height) - ship_height)
        number_aliens = available_screen_y // (2 * alien_height)
        # 计算一行多少外星人
        available_screen_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_screen_x // (2* alien_width)
        rows = random.randint(1, number_aliens);
        for row in range(rows):
            cloumns = random.randint(0, number_aliens_x)
            for alien_number in range(cloumns):
                alien = Alien(self)
                alien.x = alien_width +  2 * alien_width * alien_number
                alien.rect.x = alien.x
                alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
                self.aliens.add(alien)

    def _check_fleet_edges(self):
        '''判断是否有外星人到达屏幕边缘'''
        for alien in self.aliens.sprites():
            if alien._check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''整体向下移动'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_alien(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()


    def _ship_hit(self):
        # 将ship left -1
        self.stats.ships_left -= 1
        # 将子弹和外星人删除
        self.bullets.empty()
        self.aliens.empty()
        # 创建新的外星人和飞船
        self._create_fleet()
        self.ship.center_ship()
        # 暂停
        sleep(0.5)

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
