""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 8


def draw_doraemon(x, y):
    # Cuerpo
    arcade.draw_circle_filled(x, y, 70, arcade.color.BLUE)

    # Vientre
    arcade.draw_circle_filled(x, y - 10, 50, arcade.color.WHITE)

    # Cabeza
    arcade.draw_circle_filled(x, y + 80, 45, arcade.color.BLUE)
    arcade.draw_circle_filled(x - 25, y + 85, 10, arcade.color.WHITE)

    # Ojos
    arcade.draw_circle_filled(x - 20, y + 85, 3, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 20, y + 85, 3, arcade.color.BLACK)

    # Nariz
    arcade.draw_circle_filled(x, y + 75, 7, arcade.color.RED)

    # Boca
    arcade.draw_arc_filled(x, y + 70, 30, 30, arcade.color.WHITE, 0, 180)

    # Manos
    arcade.draw_circle_filled(x - 60, y - 20, 20, arcade.color.BLUE)
    arcade.draw_circle_filled(x + 60, y - 20, 20, arcade.color.BLUE)

    # Pies
    arcade.draw_circle_filled(x - 30, y - 80, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 30, y - 80, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 30, y - 80, 10, arcade.color.BLUE)
    arcade.draw_circle_filled(x + 30, y - 80, 10, arcade.color.BLUE)

    # Antenas
    arcade.draw_rectangle_filled(x - 15, y + 120, 5, 40, arcade.color.BLUE)
    arcade.draw_circle_filled(x - 15, y + 140, 10, arcade.color.BLUE)
    arcade.draw_rectangle_filled(x + 15, y + 120, 5, 40, arcade.color.BLUE)
    arcade.draw_circle_filled(x + 15, y + 140, 10, arcade.color.BLUE)


class Personaje:
    def __init__(self, position_x, position_y, change_x, change_y, radius):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def draw(self):
        draw_doraemon(self.position_x, self.position_y)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class Personaje2:
    def __init__(self, position_x, position_y, change_x, change_y):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        draw_doraemon(self.position_x, self.position_y)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Create our ball
        self.ball = Personaje(50, 50, 0, 0, 100)

    def on_draw(self):
        # Color del fondo
        arcade.set_background_color(arcade.color.SKY_BLUE)

        arcade.start_render()

        # Dibujar tierra
        arcade.draw_rectangle_filled(300, 100, 1000, 300, arcade.color_from_hex_string("#38ab15"))

        # -----Dibujar casa------
        # Fachada
        arcade.draw_rectangle_filled(400, 300, 250, 250, arcade.color.RED)
        arcade.draw_rectangle_outline(400, 300, 250, 250, arcade.color.BLACK, 3)

        # Tejado
        arcade.draw_triangle_filled(400, 525, 250, 425, 550, 425, arcade.color.RED_DEVIL)
        arcade.draw_triangle_outline(400, 525, 250, 425, 550, 425, arcade.color.BLACK, 3)

        # Puerta
        arcade.draw_rectangle_filled(400, 235, 60, 120, arcade.color_from_hex_string("#995a02"))
        arcade.draw_rectangle_outline(400, 235, 60, 120, arcade.color.BLACK, 3)
        arcade.draw_circle_filled(380, 230, 5, arcade.color.YELLOW)
        arcade.draw_circle_outline(380, 230, 5, arcade.color.BLACK, 3)

        # Ventana
        arcade.draw_ellipse_filled(330, 375, 55, 60, arcade.color.BABY_BLUE)
        arcade.draw_ellipse_filled(470, 375, 55, 60, arcade.color.BABY_BLUE)
        arcade.draw_ellipse_outline(330, 375, 55, 60, arcade.color.BLACK, 3)
        arcade.draw_ellipse_outline(470, 375, 55, 60, arcade.color.BLACK, 3)

        # -----Dibujar sol-----
        arcade.draw_circle_filled(700, 525, 50, arcade.color_from_hex_string("#fff700"))
        arcade.draw_circle_outline(700, 525, 50, arcade.color.BLACK, 3)

        # Bola
        self.ball.draw()

        # --- Finish drawing ---
        arcade.finish_render()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
