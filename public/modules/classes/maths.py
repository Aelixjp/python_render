import math

def toRads(deg):
    return (math.pi / 180) * deg

def rotateX(degrees):
    return [
        [1, 0                 , 0                  ],
        [0, math.cos(degrees) , -math.sin(degrees) ],
        [0, math.sin(degrees) , math.cos(degrees)  ]
    ]

def rotateY(degrees):
    return [
        [math.cos(degrees) , 0 , math.sin(degrees) ],
        [0                 , 1 , 0                 ],
        [-math.sin(degrees), 0 , math.cos(degrees) ]
    ]

def rotateZ(degrees):
    return [
        [math.cos(degrees) , -math.sin(degrees) , 0 ],
        [math.sin(degrees) , math.cos(degrees)  , 0 ],
        [0                 , 0                  , 1 ]
    ]