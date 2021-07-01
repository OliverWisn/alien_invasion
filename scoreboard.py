import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """
    Class is destined for the providing the information about 
    the score.
    """

    def __init__(self, ai_game):
        """Initialization of the attributes that concern the score."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Settings of the font for the information that concern 
        # the score and the level.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 32)

        # Preparation of the initial images with the scores.
        self.prep_score()
        self.prep_high_score()

        # Preparation of the initial image with the level.
        self.prep_level()

        # Preparation of the images with the spaceships that leave for 
        # the gamer.
        self.prep_ships()

    def prep_score(self):
        """Conversion of the score to the rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "Points: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, 
            self.text_color, self.settings.bg_color)

        # Displaying of the score in the right top corner of 
        # the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """
        Conversion of the best score in the game to the rendered image.
        """
        high_score = round(self.stats.high_score, -1)
        high_score_str = "Best score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, 
            self.text_color, self.settings.bg_color)

        # Displaying of the best score in the game in the center near 
        # of the top edge of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check if we have the new best score so far in the game."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """
        Conversion of the number of the level of the game to 
        the rendered image.
        """
        game_level = str(self.stats.level)
        level_str = "Level: {}".format(game_level)
        self.level_image = self.font.render(level_str, True, 
            self.text_color, self.settings.bg_color)

        # The number of the level is displayed under the actual score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Displaying of the spaceships that leave for the gamer"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """
        Displaying  of the score, the level and the spaceships of 
        the gamer on the screen.
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)