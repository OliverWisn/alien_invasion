import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    Class is representing a single spaceship of the alien in 
    the fleet.
    """

    def __init__(self, ai_game):
        """
        Initialization of the spaceship of the alien and the defining 
        of his initial location.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Reading out of the image of the spaceship of the alien and 
        # taking its rectangle.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Appearing of the new spaceship of the alien near the top left 
        # corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing of the exactly horizontal location of the spaceship 
        # of the alien.
        self.x = float(self.rect.x)

    def check_edges(self):
        """
        Return the value True if the spaceship of the alien come 
        across the edge of the screen.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the spaceship of the alien to the right or to the left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x