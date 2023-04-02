import arcade
import math

def hex_to_color_list(colors: list()):
    '''
    toma una lista de strings con códigos de colores en HEX
    y los convierte a colores compatibles con arcade
    '''
    return {i+1: arcade.color_from_hex_string(c) for i, c in enumerate(colors)}


REDS = hex_to_color_list(['20071e', '370617', '6a040f', '9d0208', 'd00000', 'dc2f02', 'e85d04', 'f48c06', 'faa307', 'ffba08'])
'''paleta predefinida,\ntonos ROJOS.\n(obtenidas de coolors.co)'''
YELLOWS = hex_to_color_list(['ff7b00', 'ff8800', 'ff9500', 'ffa200', 'ffaa00', 'ffb700', 'ffc300', 'ffd000', 'ffdd00', 'ffea00'])
'''paleta predefinida,\ntonos AMARILLOS.\n(obtenidas de coolors.co)'''
BLUES = hex_to_color_list(['012a4a', '013a63', '01497c', '014f86', '2a6f97', '2c7da0', '468faf', '61a5c2', '89c2d9', 'a9d6e5'])
'''paleta predefinida,\ntonos AZULES.\n(obtenidas de coolors.co)'''


def draw_fractal_tree(x, y, length, angle, depth, l_angle = 30, r_angle = 50, colors = {}):
    '''
    dibuja una linea del árbol si la profundidad es mayor a 0,
    y se llama recursivamente para dibuja las ramificaciones faltantes
    '''
    if depth == 0:
        return

    x2 = x + length * math.cos(math.radians(angle))
    y2 = y + length * math.sin(math.radians(angle))

    arcade.draw_line(x, y, x2, y2, colors.get(depth, arcade.color.WHITE), depth + 1)

    draw_fractal_tree(x2, y2, length * 0.7, angle + l_angle, depth - 1, l_angle, r_angle, colors)
    draw_fractal_tree(x2, y2, length * 0.7, angle - r_angle, depth - 1, l_angle, r_angle, colors)


if __name__ == "__main__":
    
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 650
    SCREEN_TITLE = "Árbol"

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()

    draw_fractal_tree(SCREEN_WIDTH/2, 30, 180, 80, 8, 25, 10, colors=YELLOWS)

    arcade.finish_render()
    arcade.run()
    