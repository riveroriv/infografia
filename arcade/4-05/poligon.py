import arcade
import numpy as np
import math

class Poligon:
    def __init__(self, vertices, color = arcade.color.RED):
        self.color = color
        self.vertices = vertices
    
    def draw(self):
        arcade.draw_polygon_outline(
            self.vertices,
            self.color,
            4
            )
    
    def move(self, x: int, y: int):
        for i, v in enumerate(self.vertices):
            self.vertices[i] = (v[0]+x, v[1]+y)
    
    def transform(self, matrix):
        ver_list = [[v[0],v[1],1] for v in self.vertices]
        ver_matrix = np.transpose(np.array(ver_list))

        new_matrix = np.dot(matrix, ver_matrix)
        new_matrix_t = new_matrix_2 = np.transpose(new_matrix)

        new_vertices = [(v[0], v[1]) for v in new_matrix_t]
        self.vertices = new_vertices
    
    def translate(self, dx, dy):
        self.transform(np.array([
            [   1,  0,  dx  ],
            [   0,  1,  dy  ],
            [   0,  0,  1   ]
            ]))
    
    def rotate(self, deg):
        deg = math.radians(deg)
        self.transform(np.array([
            [   math.cos(deg),    -math.sin(deg),   0   ],
            [   math.sin(deg),    math.cos(deg),    0   ],
            [   0,                  0,              1   ]
            ]))
    
    def rotate_center(self, deg):
        #center = [sum(v[i] for v in self.vertices) / len(self.vertices) for i in range(2)]
        ver_array = np.array(self.vertices)
        center = np.sum(ver_array, axis=0) / ver_array.shape[0]

        self.translate(-center[0], -center[1])
        
        deg = math.radians(deg)
        self.transform(np.array([
            [   math.cos(deg),    -math.sin(deg),   0   ],
            [   math.sin(deg),    math.cos(deg),    0   ],
            [   0,                  0,              1   ]
            ]))
        
        self.translate(center[0], center[1])
    
    def scale(self, sx, sy):
        self.transform(np.array([
            [   sx, 0,  0   ],
            [   0,  sy, 0   ],
            [   0,  0,  1   ]
            ]))


if __name__ == '__main__':
    """
    poly = Poligon([(40,50),(180,70),(120,300)])
    
    tra = np.array([1,0,100], [0,1,100], [0,0,1])
    poly.transform(tra)
    """