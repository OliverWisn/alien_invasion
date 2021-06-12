import pygame.font

class Button:
    """
    Class dedicated to the displaying of the button with the message on 
    the center of the screen.
    """
    def __init__(self, ai_game, screen, msg):
        """Initialization of the attributes of the button."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Defining of the dimensions of the button and his attributes.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Creation of the rectangle of the button and the centering 
        # him.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message displaying through the button must be display only 
        # one time.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
        Placing of the message on the generated image and the centering 
        of the text of the message on the button.
        """
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Displaying of the empty button and next the message on it.
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)