from shape import Shape
from vector import Vector
from utils import scale, product, minus
import math

class Sphere(Shape):

    def __init__(self, radius, center: Vector, color):
        super().__init__(color)
        self.radius = radius
        self.center = center

    
    def intersect(self, p0: Vector, dr: Vector):
        
        t1: float
        t2: float

        w = minus(p0, self.center)

        a = product(dr, dr)
        b = 2 * product(w, dr)
        c = product(w,w) - math.pow(self.radius,2)

        delta = math.pow(b, 2) - 4 * a * c
        
        if delta < 0:
            return (math.inf, math.inf)
        
        t1 = (-b + math.sqrt(delta))/(2*a)
        
        t2 = (-b - math.sqrt(delta))/(2*a)

        return (t1, t2)

        
