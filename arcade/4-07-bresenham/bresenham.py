def get_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    if x0 < x1:
        x_step = 1
    else:
        x_step = -1
    
    if y0 < y1:
        y_step = 1
    else:
        y_step = -1
    
    Pk = dx - dy
    
    while (x0 != x1) or (y0 != y1):
        points.append((x0, y0))
        Pk2 = 2 * Pk
        
        if Pk2 > -dy:
            Pk -= dy
            x0 += x_step
        
        if Pk2 < dx:
            Pk += dx
            y0 += y_step 
        
    points.append((x0, y0))
    return points

def get_polygon(vertices):
    points = []
    for i in range(len(vertices)):
        current_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % len(vertices)]
        line_points = get_line(current_vertex[0], current_vertex[1], next_vertex[0], next_vertex[1])
        points += line_points
    return points


if __name__ == "__main__":
    print(get_polygon([(15, 15), (30, 30), (15, 45)]))