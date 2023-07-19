import math
from turtle import shape
import pygame

from public.modules.classes.maths import rotateX, rotateY, rotateZ, toRads
from public.modules.classes.Utils import mat_mult, printArr
from public.modules.Shapes.cube import Cube
from public.modules.classes.Screen import Screen

FPS = 75
SCREEN_DIM = (1280, 720)
SCREEN_COLOR = (0, 0, 0, 0)
WINDOW_TITLE = "Renderizador de graficos 3D"

cube = Cube()
cube.grow(50)
#cube.pos.x += 100

cube2 = Cube()
cube2.grow(50)

distance = 10

anglex = 212.96
angley = 0
anglez = 0

'''mat_a = [
    [-2, 3],
    [-5, 1],
    [0 ,-6]
]

mat_b = [
    [1, -5, 0],
    [-8, 9, 2]
]

print(mat_mult(mat_a, mat_b))
exit()'''

def rotateShape(shapePoints, pos, anglex, angley, anglez):
    #Rotated version
    #rotated = mat_mult(shapePoints, 1)
    rotated = mat_mult(shapePoints, rotateX(toRads(anglex)))
    rotated = mat_mult(rotated, rotateY(toRads(angley)))
    rotated = mat_mult(rotated, rotateZ(toRads(anglez)))

    proyected = rotated

    proyection_m = [
        [1, 0],
        [0, 1],
        [0, 0]
    ]
    for i in range(len(proyected)):
        proyected[i][0] += pos.x
        proyected[i][1] += pos.y
        proyected[i][2] += pos.z

        #z = 1 / (distance - (rotated[i][2] / 200))
        z = proyected[i][2] + distance

        #m = mat_mult([rotated[i]], proyection_m)

        #print(proyected)

        #rotated[i][0] += (SCREEN_DIM[0] / 2)
        #rotated[i][1] += (SCREEN_DIM[1] / 2)

        '''m[0][0] += (SCREEN_DIM[0] / 2)
        m[0][1] += (SCREEN_DIM[1] / 2)'''

        '''m[0][0] += (SCREEN_DIM[0] / 2) #+ pos.x
        m[0][1] += (SCREEN_DIM[1] / 2) #+ pos.y'''

        proyected[i][0] /= z
        proyected[i][1] /= z

        proyected[i][0] *= 100
        proyected[i][1] *= 100

        proyected[i][0] += (SCREEN_DIM[0] / 2)
        proyected[i][1] += (SCREEN_DIM[1] / 2)

    proyected = mat_mult(proyected, proyection_m)

    return proyected

def normalizeAngle(angle):
    if angle > 0:
        angle %= 360
    else:
        angle = 360 - angle
    
    return angle

def main():
    global distance
    global anglex
    global angley
    global anglez

    # pygame setup
    pygame.init()

    screen = Screen(SCREEN_DIM, SCREEN_COLOR, WINDOW_TITLE, FPS)

    while screen.running:
        screen.paint()
        screen.listenForEvents()
        
        '''screen.graphics.drawCircle('red', 1, (200, 200), 20)
        screen.graphics.drawRect('blue', 1, 400, 200, 60)
        screen.graphics.drawPolygon('green', 1, ((400, 300), (450, 350), (400, 400)))'''

        if screen.eventHandler.key_map["A"]:
            cube.pos.x += 3
            cube2.pos.x += 3
        if screen.eventHandler.key_map["D"]:
            cube.pos.x -= 3
            cube2.pos.x -= 3
        if screen.eventHandler.key_map["W"]:
            distance -= 0.01
        if screen.eventHandler.key_map["S"]:
            distance += 0.01
        if screen.eventHandler.key_map["A_8"]:
            cube.pos.y -= 3
            cube2.pos.y -= 3
        if screen.eventHandler.key_map["A_5"]:
            cube.pos.y += 3
            cube2.pos.y += 3
        if screen.eventHandler.key_map["A_UP"]:
            anglex -= 1
        if screen.eventHandler.key_map["A_DOWN"]:
            anglex += 1
        if screen.eventHandler.key_map["A_LEFT"]:
            angley -= 1
        if screen.eventHandler.key_map["A_RIGHT"]:
            angley += 1

        normalizeAngle(anglex)
        normalizeAngle(angley)
        normalizeAngle(anglez)
        
        cube.normalizeAngle()
        cube2.normalizeAngle()

        #Original points based
        #screen.graphics.drawPolygon('blue', 1, cube.proyected_points[0])

        for i in range(1):
            shape = cube.points[i]

            proyected = rotateShape(shape, cube.pos, anglex, angley, anglez)
            screen.graphics.drawPolygon('orange', 1, proyected)

        '''for i in range(len(cube2.points)):
            shape = cube2.points[i]

            proyected = rotateShape(shape, cube2.pos, anglex, angley, anglez)
            screen.graphics.drawPolygon('blue', 1, proyected)'''

        '''screen.graphics.drawPolygon('orange', 1, proyectedShape)
        screen.graphics.drawPolygon('blue', 1, proyectedShape2)
        screen.graphics.drawPolygon('green', 1, proyectedShape3)
        screen.graphics.drawPolygon('white', 1, proyectedShape4)
        screen.graphics.drawPolygon('red', 1, proyectedShape5)
        screen.graphics.drawPolygon('aqua', 1, proyectedShape6)'''
        
        #print(proyected)
        
        #screen.graphics.drawPolygon('orange', 1, cube.proyected_points[1])

        # flip() the display to put your work on screen
        pygame.display.flip()
        screen.tick()

    pygame.quit()


main()