import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"

# Funciones para dibujar
def snowman():
    arcade.draw_rectangle_filled(
        SCREEN_WIDTH / 2 + 80,
        (SCREEN_HEIGHT / 2) - 20,
        6,
        100,
        arcade.color.BROWN,
        tilt_angle= 50
    )

    arcade.draw_circle_filled(
        SCREEN_WIDTH / 2, 
        (SCREEN_HEIGHT / 4) + 230, 
        40, 
        arcade.color.WHITE
        )
    arcade.draw_circle_filled(
        SCREEN_WIDTH / 2, 
        (SCREEN_HEIGHT / 4) + 140, 
        70, 
        arcade.color.WHITE
        )
    arcade.draw_circle_filled(
        SCREEN_WIDTH / 2, 
        SCREEN_HEIGHT / 4, 
        100, 
        arcade.color.WHITE
        )

    # ojos
    arcade.draw_circle_filled(
        SCREEN_WIDTH / 2 + 25, 
        (SCREEN_HEIGHT / 4) + 242,
        5, 
        arcade.color.BLACK
        )
    arcade.draw_circle_filled(
        SCREEN_WIDTH / 2 - 5, 
        (SCREEN_HEIGHT / 4) + 240,
        5, 
        arcade.color.BLACK
        )

    arcade.draw_circle_filled(
        SCREEN_WIDTH / 2 + 45, 
        (SCREEN_HEIGHT / 4) + 10,
        5, 
        arcade.color.BLACK
        )
    arcade.draw_circle_filled(
        SCREEN_WIDTH / 2 + 35, 
        (SCREEN_HEIGHT / 4) + 80,
        5, 
        arcade.color.BLACK
        )
    arcade.draw_circle_filled(
        SCREEN_WIDTH / 2 + 37, 
        (SCREEN_HEIGHT / 4) + 140,
        5, 
        arcade.color.BLACK
        )

    # nariz
    arcade.draw_triangle_filled(
        SCREEN_WIDTH / 2 + 10,  (SCREEN_HEIGHT / 4) + 235,
        SCREEN_WIDTH / 2 + 40,  (SCREEN_HEIGHT / 4) + 230,
        SCREEN_WIDTH / 2 + 10,  (SCREEN_HEIGHT / 4) + 225,
        arcade.color.ORANGE
    )
    # sombrero
    arcade.draw_rectangle_filled(
        SCREEN_WIDTH / 2,
        (SCREEN_HEIGHT / 4) + 300,
        50,
        70,
        arcade.color.SCARLET
    )
    arcade.draw_rectangle_filled(
        SCREEN_WIDTH / 2,
        (SCREEN_HEIGHT / 4) + 260,
        100,
        10,
        arcade.color.SCARLET
    )
    # brazo
    arcade.draw_rectangle_filled(
        SCREEN_WIDTH / 2 - 80,
        (SCREEN_HEIGHT / 2) - 30,
        6,
        100,
        arcade.color.BROWN,
        tilt_angle= -50
    )


if __name__ == "__main__":
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

    snowman()

    # finalizar render
    arcade.finish_render()

    # Correr el programa
    arcade.run()