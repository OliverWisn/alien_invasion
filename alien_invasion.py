import sys

import pygame

from settings import Settings

class AlienInvasion:
    """General class dedicated to the managing the resources and the 
way the game works."""

    def __init__(self):
        """The game initialization and the setting up its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, \
            self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start of the main loop of the game"""
        while True:
            # Waiting for the press a key or a mouse button.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # The screen refresh in the time of the every loop 
            # iteration.
            self.screen.fill(self.settings.bg_color)

            # Display of the last modified screen.
            pygame.display.flip()

if __name__ == '__main__':
    # Setting up of the object of the game and the start-up of 
    # the game.
    ai = AlienInvasion()
    ai.run_game()