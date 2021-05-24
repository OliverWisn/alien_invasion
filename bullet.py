import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Class dedicated to the managing the bullets that are shooted by 
    the ship.
    """

    def __init__(self, ai_game):
        """
        Setting up of the object of the bullet in the actual location 
        of the ship.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Setting up of the rectangle of the bullet in the point(0, 0) 
        # and next define for him the proper location.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self. rect.midtop = ai_game.ship.rect.midtop

        # The location of the ship is defined by means of the float 
        # value.
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet around the screen."""
        # Updating of the location of the bullet.
        self.y -= self.settings.bullet_speed
        # Updating of the location of the rectangle of the bullet.
        self.rect.y = self.y

    def draw_bullet(self):
        """Displaying of the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)