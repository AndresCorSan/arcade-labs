import arcade

# Abrir ventana
arcade.open_window(800, 600, "Lab-02 Draw")

# Color del fondo
arcade.set_background_color(arcade.color.SKY_BLUE)

# Empezar a dibujar
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



# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

