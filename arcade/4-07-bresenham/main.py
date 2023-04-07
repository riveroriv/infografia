import arcade
from bresenham import get_line, get_polygon

# definicion de constantes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Bresenham"


BACK_COLOR = arcade.color_from_hex_string("463f3a")
GRID_COLOR = arcade.color_from_hex_string("8a817c")
LINE_COLOR = arcade.color_from_hex_string("e0afa0")
SCALED_COLOR = arcade.color_from_hex_string("f4f3ee")


class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(BACK_COLOR)
        self.pixel_size = 20

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()

        self.draw_both_line(20, 10, 5, 35)
        self.draw_both_line(3, 2, 10, 20)
        self.draw_both_line(10, 2, 10, 10)
        self.draw_both_line(15, 5, 25, 5)
        self.draw_both_line(15, 26, 25, 30)

        self.draw_both_polygon([(35, 5), (25, 20), (35, 25), (45, 20)])
        

    def draw_both_line(self, x0, y0, x1, x2):
        self.draw_points(get_line(x0, y0, x1, x2), LINE_COLOR)
        self.draw_scaled_line(x0, y0, x1, x2, SCALED_COLOR)
    
    def draw_both_polygon(self, points):
        self.draw_points(get_polygon(points), LINE_COLOR)
        self.draw_scaled_polygon(points, SCALED_COLOR)

    def draw_grid(self):
        # lineas verticales
        
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT,
                GRID_COLOR
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2,
                GRID_COLOR
            )

    def draw_points(self, points,  color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_line(self, x0, y0, x1, y1, color):
        arcade.draw_line(
            x0 * self.pixel_size, 
            y0 * self.pixel_size, 
            x1 * self.pixel_size, 
            y1 * self.pixel_size,
            color,
            5
        )
    
    def draw_scaled_polygon(self, points, color):
        arcade.draw_polygon_outline(
            [(v[0]*self.pixel_size, v[1]*self.pixel_size) for v in points],
            color,
            5
            )


if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()