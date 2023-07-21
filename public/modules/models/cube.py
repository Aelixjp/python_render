from ..classes.Shape import Shape
from ..classes.Utils import createVector3, loadJSON

class Cube(Shape):
    def __init__(self, color = "white", x = 0, y = 0, z = 0) -> None:
        self.color = color
        self.pos = createVector3((x, y, z))
        self.rotation = createVector3((x, y, z))
        self.points = loadJSON("cube")