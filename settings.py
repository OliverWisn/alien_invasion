class Settings:
    """Class is destined for the storage of the all settings of the 
game."""

    def __init__(self):
        """Initialization of the settings of the game."""

        # Settings of the screen.
        self.screen_width = 1350
        self.screen_height = 700
        self.bg_color = (184, 134, 11)
        
        # Settings relative to the ship.
        self.ship_speed = 1.5

        # Settings relative to the bullet.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)