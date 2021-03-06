class GameStats:
    """
    Monitoring of the statistical dates in the game "Alien Invasion".
    """

    def __init__(self, ai_game):
        """Initialization of the statistical dates."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start-up of the game "Alien Invasion" in the active state.
        self.game_active = False

        # The best score should never be reset.
        with open("save/save_high_score.txt") as file_object:
            self.high_score = file_object.read()
            self.high_score = int(self.high_score)

    def reset_stats(self):
        """
        Initialization of the statistical dates that can change in 
        the time of the game.
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1