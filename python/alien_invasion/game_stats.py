class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_start()
    def reset_start(self):
        self.ships_left = self.settings.ship_limit