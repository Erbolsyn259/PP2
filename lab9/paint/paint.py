import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    erase = False
    rectangle = False
    circle = False
    squere = False
    RightTriangle = False
    EquilateralTriangle = False
    rhombus = False

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                if event.key == pygame.K_BACKSPACE:
                    erase = not erase
                elif event.key == pygame.K_w:
                    rectangle = not rectangle
                elif event.key == pygame.K_s:
                    squere = not squere
                elif event.key == pygame.K_o:
                    RightTriangle = not RightTriangle
                elif event.key == pygame.K_e:
                    EquilateralTriangle = not EquilateralTriangle
                elif event.key == pygame.K_c:
                    circle = not circle
                elif event.key == pygame.K_r:
                    rhombus = not rhombus
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                if erase:
                    points = [p for p in points if (p[0] - position[0]) ** 2 + (p[1] - position[1]) ** 2 > radius ** 2]# стиралка работает только если стирать пожалуста стирайте интенсивнее
                else:                                                                                                  #двигате мышкой туда сюда по screen
                    points = points + [position]
                    points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode,rectangle,circle,squere,RightTriangle,EquilateralTriangle,rhombus)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)
def drawEquilateralTriangle(screen, color, mouse_pos):
    #define the points in a uint space
    x = mouse_pos[0]
    y = mouse_pos[1]
    triangle_size = 50

    # Calculate the triangle's vertices
    triangle_points = [
        (x, y - triangle_size - 100),
        (x - triangle_size, y + triangle_size),
        (x + triangle_size, y + triangle_size),
    ]

    # Draw the triangle
    pygame.draw.polygon(screen, color, triangle_points)  


def drawLineBetween(screen, index, start, end, width, color_mode,rectangle,circle,squere,RightTriangle,EquilateralTriangle,rhombus):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if rectangle:
            rect =pygame.Rect(x,y,200,100)
            pygame.draw.rect(screen, color, rect, 3)
        elif circle:
            pygame.draw.circle(screen, color, (x, y), 100, 3)
        elif squere:
            rect =pygame.Rect(x,y,150,150)
            pygame.draw.rect(screen, color, rect, 3)
        elif rhombus:
            # Calculate the rhombus's vertices
            rhombus_points = [
                (x, y - 100),
                (x + 100, y),
                (x, y + 100),
                (x - 100, y),
            ]
            # Draw the triangle
            pygame.draw.polygon(screen, color, rhombus_points,3)
        elif RightTriangle:
            # Calculate the triangle's vertices
            triangle_points = [
                (x, y - 100),
                (x, y + 100),
                (x + 100, y + 100),
            ]

            # Draw the triangle
            pygame.draw.polygon(screen, color, triangle_points,3)
        elif EquilateralTriangle:
            # Calculate the triangle's vertices
            triangle_points = [
                (x, y - 100),
                (x - 100, y + 100),
                (x + 100, y + 100),
            ]

            # Draw the triangle
            pygame.draw.polygon(screen, color, triangle_points,3)
        else:
            pygame.draw.circle(screen, color, (x, y), width)

main()