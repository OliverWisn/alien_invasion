import pygame

class Ship:
    """Class dedicated to the managing the spaceship."""

    def __init__(self, ai_game):
        """Initialization of the spaceship and his initial location."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Reading out of the image of the spaceship and taking its 
        # rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new spaceship appear on the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Horizontal location of the ship is stored in 
        # the floating-point number form.
        self.x = float(self.rect.x)

        # Options that indicate the moving of the ship.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Updating of the location of the ship on the basis of options 
        that indicate the moving of the ship.
        """
        # Update of the value of the coordinate x of the ship.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update of the object rect on the basis of the value of 
        # self.x.
        self.rect.x = self.x

    def blitme(self):
        """Displaying of the spaceship in his actual location."""
        self.screen.blit(self.image, self.rect)