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
# Tejado
arcade.draw_triangle_filled(400, 525, 250, 425, 550, 425, arcade.color.GREEN)
# Puerta
arcade.draw_rectangle_filled(400, 235, 60, 120, arcade.color_from_hex_string("#995a02"))
arcade.draw_circle_filled(380, 230, 5, arcade.color.YELLOW)
# Ventana




# Dibujar sol
arcade.draw_circle_filled(700, 525, 50, arcade.color_from_hex_string("#fff700"))


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

