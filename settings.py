class Settings():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=750
        self.bg_color=(230,230,230)

        self.yukino_limit=3
        
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3

        self.speedup_scale=1.1
        self.score_scale=10
        self.initialize_dynamic_settings()

        self.stop_time=1

    def initialize_dynamic_settings(self):
        self.yukino_speed_factor=1
        self.bullet_speed_factor=3
        self.teacher_speed_factor=0.5
        self.fleet_direction=1
        self.teacher_points=50
        self.fleet_drop_speed=10
    
    def increase_speed(self):
        self.yukino_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.teacher_speed_factor*=self.speedup_scale
        self.fleet_drop_speed*=self.speedup_scale
        self.teacher_points=self.teacher_points+self.score_scale
