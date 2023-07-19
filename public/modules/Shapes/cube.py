from ..classes.Utils import createVector3
from ..classes.Utils import mat_mult

class Cube:
    
    def __init__(self, x = 0, y = 0, z = 0) -> None:
        self.angle = 0
        self.pos = createVector3((x, y, z))

        self.proyection_matrix = [
            [1, 0],
            [0, 1],
            [0, 0]
        ]

        '''self.points = [
            #Front face
            [
                [-1, -1, 1],
                [1 , -1, 1],
                [1 ,  1, 1],
                [-1,  1, 1]
            ],
            #Back face
            [
                [-1, -1, -1],
                [1 , -1, -1],
                [1 ,  1, -1],
                [-1,  1, -1]
            ],
            #Union line 1
            [
                [-1, -1,  1],
                [-1, -1, -1]
            ],
            #Union line 2
            [
                [1, -1,  1],
                [1, -1, -1]
            ],
            #Union line 3
            [
                [1, 1,  1],
                [1, 1, -1]
            ],
            #Union line 4
            [
                [-1, 1,  1],
                [-1, 1, -1]
            ]
        ]'''

        self.points = [
            [
                [-1, -1, -1],
                [ 1, -1, -1],
                [ 1,  1, -1],
                [-1,  1, -1]
            ],
            [
                [-1, -1, 1],
                [ 1, -1, 1],
                [ 1,  1, 1],
                [-1,  1, 1]
            ],
            [
                [-1, -1, 1],
                [-1, -1, -1]
            ],
            [
                [1, -1, 1],
                [1, -1, -1]
            ],
            [
                [1, 1, 1],
                [1, 1, -1]
            ],
            [
                [-1, 1, 1],
                [-1, 1, -1]
            ]
        ]

        self.proyected_points = self.points

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