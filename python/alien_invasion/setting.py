class Settings:
    def __init__(self):
        self.bg_color = (230,230,230)
        self.screen_width = 1200
        self.screen_height = 800
        # 飞船移动速度
        self.ship_speed = 1.5
        self.ship_limit = 3
        # 子弹设置
        self.bullet_color=(60,60,60)
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed = 1.0
        # 外星人向下移动速度
        self.fleet_drop_speed = 10
        # 1为向右移动，-1向左移动
        self.fleet_direction = 1