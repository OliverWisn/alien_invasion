import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """
    General class dedicated to the managing the resources and the way 
    the game works.
    """

    def __init__(self):
        """The game initialization and the setting up its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Setting up of the object that keep the statistical dates 
        # relative to the game and setting up of the object of 
        # the class Scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Creation of the button Play
        self.play_button = Button(self, self.screen, "Play")

    def run_game(self):
        """Start of the main loop of the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()

    def _check_events(self):
        """
        Reaction for the events generated by the keyboard and 
        the mouse.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.stats.game_active:
                    self._check_mouse_buttons(event)
                else:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        self._check_play_button(mouse_pos)

        # Check for the pressed keys that didn't release.
        self._check_pressed_keys()

    def _check_keydown_events(self, event):
        """Reaction for the pressing of the key."""
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if self.stats.game_active:
                self._fire_bullet()
        elif event.key == pygame.K_p:
            if not self.stats.game_active:
                self.stats.game_active = True

    def _check_keyup_events(self, event):
        """Reaction for the releasing of the key."""
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_pressed_keys(self):
        """Reaction for the pressed keys that didn't release."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.ship.moving_right = True
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.ship.moving_left = True

    def _check_mouse_buttons(self, event):
        """Reaction for the pressing of the left mouse button."""
        if event.button == 1:
            self._fire_bullet()

    def _check_play_button(self, mouse_pos):
        """
        Running of the new game as the reaction for the clicking of 
        the left mouse button on the button Play that is displaying on 
        the screen.
        """
        if self.play_button.rect.collidepoint(mouse_pos):
            # Reseting of the dynamic settings of the game.
            self.settings.initialize_dynamic_settings()

            # Reseting of the statistical data of the game.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Removal of the content of the lists aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Creation of the new full fleet of the spaceships of 
            # the aliens and the centering of the ship of the gamer.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """
        Creation of a new bullet and add him to the group of 
        the bullets.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 

    def _update_bullets(self):
        """
        Updating of the location of the bullets and deletion of 
        the bullets that are invisible.
        """
        # Updating of the location of the bullets.
        self.bullets.update()

        # Deletion of the bullets that are beyond of the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_allien_collisions()

    def _check_bullet_allien_collisions(self):
        """
        Reaction for the collision between the bullet and the spaceship 
        of the alien.
        """
        # Disposal of all bullets and all spaceships of the aliens 
        # between which was the collision.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Removal of the existing bullets, the acceleration of 
            # the game and the creation of the new fleet of 
            # the spaceships of the aliens.
            self.bullets.empty()
            self.settings.increase_speed()
            self._create_fleet()

            # Increment the number of the level.
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """
        Creation of the full fleet of the spaceships of the aliens.
        """
        # Creation of the spaceship of the alien and the seting 
        # the number of the spaceships of the aliens that fits in 
        # a row.
        # The distance between the particular spaceships of the aliens 
        # is equal to the width of the rectangle of the spaceship of 
        # the alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avialable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avialable_space_x // (2 * alien_width)

        # Seting how many rows of the spaceships of the aliens fits in 
        # the screen.
        ship_height = self.ship.rect.height
        avialable_space_y = (self.settings.screen_height - 
            (6 * alien_height) - ship_height)
        number_rows = avialable_space_y // (2 * alien_height)

        # Creation of the full fleet of the spaceships of the aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number) 

    def _create_alien(self, alien_number, row_number):
        """
        Creation of the spaceship of the alien and placing him in 
        the row.
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """
        Appropriate reaction for the getting of the spaceship of 
        the alien to the edge of the screen.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        Moving of all fleet of the spaceships of the aliens down and 
        the changing of the direction of the moving of the fleet.
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """
        Check that the fleet of the spaceships of the aliens come 
        across the edge of the screen and next the updating of 
        the location of the all spaceships of the aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Detecting of the collision between the spaceship of 
        # the alien and the spaceship of the gamer.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Searching for the the aliens that reach the bottom of 
        # the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """
        Check that any spaceship of the aliens reach the bottom of 
        the screen.
        """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # The same behavior like at the hitting of 
                # the spaceship of the alien in the ship of the gamer.
                self._ship_hit()
                break

    def _ship_hit(self):
        """
        Reaction for the hitting of the spaceship of the alien in 
        the ship of the gamer.
        """
        if self.stats.ships_left > 0:
            # Decrease in the value keeps in the "ships_left" and 
            # the updating of the scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Removal of the content of the lists aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Creation of the new full fleet of the spaceships of 
            # the aliens and the centering of the ship of the gamer.
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """
        Updating of the view on the screen and the transition to 
        the new screen.
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Displaying of the information about the score.
        self.sb.show_score()

        # Displaying of the button Play only when the game is not 
        # active.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
        pygame.time.delay(self.settings.time_delay)

if __name__ == '__main__':
    # Setting up of the object of the game and the start-up of 
    # the game.
    ai = AlienInvasion()
    ai.run_game()