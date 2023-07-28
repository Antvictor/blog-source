import sys
import pygame
from setting import Settings

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

    def run_game(self):
        '''开始游戏主循环'''
        while True:
            # 监听键盘和鼠标操作
            for event in pygame.event.get():
                # 监听到退出
                if event.type == pygame.QUIT:
                    # 关闭程序
                    sys.exit()
                # 每次循环都重绘屏幕
                self.screen.fill(self.settings.bg_color)
                # 让最近绘制的屏幕可见
                pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
