from abc import ABC
from pygame import Vector3

from .Utils import mat_mult

class Shape(ABC):
    pos: Vector3
    color: str
    rotation: Vector3
    points: list

    def normalizeAngle(self):
        if self.angle > 0:
            self.angle %= 360
        else:
            self.angle = 360 - self.angle

    def translate(self, x = 0, y = 0):
        #Loop over the primes
        for i in range(len(self.points)):
            for j in range(len(self.points[i])):
                self.points[i][j][0] += x
                self.points[i][j][1] += y

    def grow(self, scaleFactor = 1):
        #Loop over the primes
        for i in range(len(self.points)):
            self.points[i] = mat_mult(self.points[i], scaleFactor)

    def proyect(self):
        #Loop over the primes
        for i in range(len(self.points)):
            #Deleting Z
            self.proyected_points[i] = mat_mult(self.proyected_points[i], self.proyection_matrix)