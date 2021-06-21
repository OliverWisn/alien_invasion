class Settings:
    """
    Class is destined for the storage of the all settings of 
    the game.
    """

    def __init__(self):
        """Initialization of the settings of the game."""

        # Settings of the screen.
        self.screen_width = 1350
        self.screen_height = 700
        self.bg_color = (70, 130, 180)
        
        # Settings relative to the ship of the gamer.
        self.ship_limit = 3

        # Settings relative to the bullet.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Settings relative to the spaceship of the alien.
        self.fleet_drop_speed = 10

        # Settings relative to the time delay of the game.
        self.time_delay = 1

        # Easy change of the game speed.
        self.speedup_scale = 1.1

        # Easy change of the points value that are awarded for 
        # the shooting down of the alien.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initialization of the settings that change in the time of 
        the game.
        """
        # Settings relative to the ship of the gamer.
        self.ship_speed = 1.5

        # Settings relative to the bullet.
        self.bullet_speed = 1.5

        # Settings relative to the spaceship of the alien.
        self.alien_speed = 0.2

        # Value "fleet_direction" amount 1 means to the right and -1 
        # means to the left.
        self.fleet_direction = 1

        # Score
        self.alien_points = 2

    def increase_speed(self):
        """
        Changing of the settings that concern the speed of the game 
        and the value of the awarded points.
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)