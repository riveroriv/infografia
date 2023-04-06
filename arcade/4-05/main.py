import arcade
import numpy as np
from poligon import Poligon

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Matrices de transformación"

class TransformWindow(arcade.Window):
    def __init__(self, poligon: Poligon):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.poligon = poligon

    def on_draw(self):
        arcade.start_render()
        self.poligon.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            #self.poligon.move(10, 10)
            #self.poligon.transform(tra)
            self.poligon.translate(20, 30)
        if symbol == arcade.key.DOWN:
            self.poligon.rotate_center(-30)
        if symbol == arcade.key.LEFT:
            self.poligon.scale(0.5,0.5)
        if symbol == arcade.key.RIGHT:
            self.poligon.scale(2,2)


if __name__ == '__main__':
    poly = Poligon([(140,200),(180,170),(120,400), (100,80)])
    app = TransformWindow(poly)
    arcade.run()