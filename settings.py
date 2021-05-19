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