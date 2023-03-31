import arcade
from hello_arcade import snowman

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "POO en arcade"

class Hola(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
    
    def on_draw(self):
        arcade.start_render()
        snowman()

if __name__ == "__main__":
    app = Hola()
    arcade.run()