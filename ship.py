import pygame

class Ship:
    """Class dedicated to the managing the spaceship."""

    def __init__(self, ai_game):
        """Initialization of the spaceship and his initial location."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Reading out of the image of the spaceship and taking its 
        # rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new spaceship appear on the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Displaying of the spaceship in his actual location."""
        self.screen.blit(self.image, self.rect)