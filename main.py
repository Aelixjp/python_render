import pygame
import math

from public.modules.classes.maths import rotateX, rotateY, rotateZ, toRads
from public.modules.classes.Utils import mat_mult
from public.modules.models.cube import Cube
from public.modules.models.pyramid import Pyramid
from public.modules.classes.Screen import Screen

FPS = 75
SCREEN_DIM = (1280, 720)
SCREEN_COLOR = (0, 0, 0, 0)
WINDOW_TITLE = "Renderizador de graficos 3D"

cube = Cube()
cube.color = "blue"
cube.grow(50)
cube.pos.x += 0

pyramid = Cube()
pyramid.pos.x += 100
pyramid.color = "orange"
pyramid.grow(50)

distance = 300
zoom = SCREEN_DIM[1]

#anglex = 212.96
anglex = 0
angley = 0
anglez = 0

objects = [cube, pyramid]

def rotateShape(shapePoints, pos, anglex, angley, anglez):
    #Rotated version
    rotated = mat_mult(shapePoints, rotateX(toRads(anglex)))
    rotated = mat_mult(rotated, rotateY(toRads(angley)))
    rotated = mat_mult(rotated, rotateZ(toRads(anglez)))

    proyected = rotated

    proyection_m = [
        [1, 0],
        [0, 1],
        [0, 0]
    ]

    #camx = 100 * math.cos(anglex)
    #camy = 0 * math.sin(angley)
    #camz = 100 * math.tan(anglez)

    for i in range(len(proyected)):
        proyected[i][0] += pos.x
        proyected[i][1] += pos.y
        proyected[i][2] += pos.z

        z = proyected[i][2] + distance

        proyected[i][0] /= z
        proyected[i][1] /= z

        proyected[i][0] *= zoom
        proyected[i][1] *= zoom

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
    global objects
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

        for i in range(len(objects)):
            obj = objects[i]

            if screen.eventHandler.key_map["A"]:
                obj.pos.x += 1
            if screen.eventHandler.key_map["D"]:
                obj.pos.x -= 1
            if screen.eventHandler.key_map["W"]:
                distance -= 1
            if screen.eventHandler.key_map["S"]:
                distance += 1
            if screen.eventHandler.key_map["A_8"]:
                obj.pos.y -= 1
            if screen.eventHandler.key_map["A_5"]:
                obj.pos.y += 1
            if screen.eventHandler.key_map["A_UP"]:
                anglex -= 1
                #obj.pos.z -= 1
            if screen.eventHandler.key_map["A_DOWN"]:
                anglex += 1
                #obj.pos.z += 1
            if screen.eventHandler.key_map["A_LEFT"]:
                angley -= 1
            if screen.eventHandler.key_map["A_RIGHT"]:
                angley += 1

        normalizeAngle(anglex)
        normalizeAngle(angley)
        normalizeAngle(anglez)

        for i in range(len(objects)):
            obj = objects[i]

            for j in range(len(obj.points)):
                shape = obj.points[j]

                proyected = rotateShape(shape, obj.pos, anglex, angley, anglez)
                screen.graphics.drawPolygon(obj.color, 1, proyected)

        # flip() the display to put your work on screen
        pygame.display.flip()
        screen.tick()

    pygame.quit()


main()