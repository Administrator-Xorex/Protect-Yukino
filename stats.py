class GameStats():
    def __init__(self,number):
        self.number=number
        self.reset_stats()
        self.game_active=False
        self.high_score=False

    def reset_stats(self):
        self.yukino_left=self.number.yukino_limit
        self.score=False
        self.level=1