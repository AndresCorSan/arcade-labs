""" Sprite Sample Program """

import random
import arcade
import math

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.6
SPRITE_SCALING_COIN = 0.3
SPRITE_SCALING_ASTEROID = 0.3

COIN_COUNT = 50
ASTEROIDS_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class Asteroid(arcade.Sprite):
    """
    This class represents the asteroids on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.asteroids_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.asteroids_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip3_orange.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            coin = Coin(":resources:images/items/gold_1.png", SPRITE_SCALING_COIN)

            coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            coin.circle_radius = random.randrange(10, 200)

            coin.circle_angle = random.random() * 2 * math.pi

            self.coin_list.append(coin)

        for j in range(ASTEROIDS_COUNT):
            asteroid = Asteroid(":resources:images/space_shooter/meteorGrey_big3.png", SPRITE_SCALING_ASTEROID)

            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)

            self.asteroids_list.append(asteroid)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.asteroids_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if len(self.coin_list) == 0:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, arcade.color.RED, 60)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        if len(self.coin_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        if len(self.coin_list) > 0:
            self.coin_list.update()
            self.asteroids_list.update()

            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

            asteroids_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.asteroids_list)
            for asteroid in asteroids_hit_list:
                asteroid.reset_pos()
                self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
