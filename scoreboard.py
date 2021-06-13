import pygame.font

class Scoreboard:
    """
    Class is destined for the providing the information about 
    the score.
    """

    def __init__(self, ai_game):
        """Initialization of the attributes that concern the score."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Settings of the font for the information that concern 
        # the score.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Preparation of the initial images with the score.
        self.prep_score()

    def prep_score(self):
        """Conversion of the score to the rendered image."""
        score_str = str(self, stats.score)
        self.score_image = self.font.render(score_str, True, 
            self.text_color, self.settings.bg_color)

        # Displaying of the score in the right top corner of 
        # the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Displaying of the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)