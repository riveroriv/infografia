import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Lineas con bresenham"

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.px = SCREEN_WIDTH / 2
        self.py = SCREEN_HEIGHT / 2
        self.step = 5
        self.score = 0
        self.points = []

    def on_draw(self):
        ''''''
        arcade.start_render()
        arcade.draw_point(self.px, self.py, arcade.color.RED, 10)
        arcade.draw_text(
            "Come los puntos",
            350,
            770,
            arcade.color.YELLOW,
            15
            )
        arcade.draw_text(
            "Score: "+str(self.score),
            700,
            35,
            arcade.color.YELLOW,
            15
            )
        if self.points:
            arcade.draw_points(self.points, arcade.color.GREEN, size = 5)

    def on_key_press(self, symbol: int, modifiers:int):
        '''
        Método para detetar teclas que han sido presionada
        el punto se mueve con las teclas de dirección
        Argumentos:
            symbol: tecla presionada
            modifiers: modificadores presionados
        '''
        
        if symbol == arcade.key.UP:
            #print('Arriba')
            self.py += self.step
        if symbol == arcade.key.DOWN:
            #print('Abajo')
            self.py -= self.step
        if symbol == arcade.key.LEFT:
            #print('Izquierda')
            self.px -= self.step
        if symbol == arcade.key.RIGHT:
            #print('Derecha')
            self.px += self.step
        
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        '''
        Método para detectar click en el mouse
        En la posición del clic se sibujará un nuevo punto
        Argumentos:
            x: coordenadas x delclic
            y: coordenadas y del clic
            button: boton del mouse presionado
            modifiers: teclas modificadoras presionadas
        '''
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(f"Agregando punto ({x, y})")
            self.points.append((x,y))

    def on_update(self, delta_time):
        '''
        Método para actualizar objetos en la app
        '''
        #print(delta_time)
        collision = self.player_is_on_foot()
        if(collision != -1):
            self.score += 1
            #print(f"Score = {self.score}")
            self.points.pop(collision)
    
    def player_is_on_foot(self):
        '''
        devuelve el índice del punto en la lista self.points si existe una colisión.
        si no existe la colisión, devuelve -1
        '''
        for i, point in enumerate(self.points):
            x,y = point
            if abs(self.px - x) < 7 and abs(self.py - y) < 7:
                return i
        return -1


if __name__ == '__main__':
    app = App()
    arcade.run()