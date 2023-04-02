import arcade
import fractal_tree as ft

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Parque"

class Parque(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
    
    def add_tree(self, x, y, length, angle, depth, l_angle = 30, r_angle = 50, colors = {}):
        ft.draw_fractal_tree(x, y, length, angle, depth, l_angle, r_angle, colors)

    def on_draw(self):
        arcade.start_render()
    
    def run(self):
        arcade.finish_render()
        arcade.run()

if __name__ == "__main__":
    app = Parque()
    app.add_tree((7.4* SCREEN_WIDTH) / 8, 170, 50, 86, 5, 80, 20)
    app.add_tree((7* SCREEN_WIDTH) / 8, 150, 70, 95, 6, 10, 50, colors=ft.BLUES)
    app.add_tree((6* SCREEN_WIDTH) / 8, 90, 120, 90, 8, 25, 25, colors=ft.REDS)
    app.add_tree((3* SCREEN_WIDTH) / 8, 10, 240, 88, 9, 60, 40, colors=ft.YELLOWS)
    app.run()