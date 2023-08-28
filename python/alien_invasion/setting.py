class Settings:
    def __init__(self):
        self.bg_color = (230,230,230)
        self.screen_width = 1200
        self.screen_height = 800
        
        # 飞船生命
        self.ship_limit = 3
        # 子弹设置
        self.bullet_color=(60,60,60)
        
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullets_allowed = 3
        # 外星人设置
        
        # 外星人向下移动速度
        self.fleet_drop_speed = 10
        # 调节游戏难度
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''初始化随游戏进度而变化的值'''
        # 飞船移动速度
        self.ship_speed = 1.5
        # 子弹速度
        self.bullet_speed = 3.0
        # 外星人速度
        self.alien_speed = 1.0

        # 1为向右移动，-1向左移动
        self.fleet_direction = 1

    def increase_speed(self):
        '''修改速度'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
