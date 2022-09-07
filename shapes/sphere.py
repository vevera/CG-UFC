from reflexivity import Reflexivity
from shapes.shape import Shape
from vector import Vector
from utils import scale, product, minus
import math


class Sphere(Shape):
    def __init__(self, radius, center: Vector, color, reflexivity: Reflexivity):
        super().__init__(reflexivity, color)
        self.radius = radius
        self.center = center

    def intersect(self, p0: Vector, dr: Vector):

        t1: float
        t2: float

        w = p0 - self.center

        a = dr * dr
        b = 2 * (w * dr)
        c = (w * w) - math.pow(self.radius, 2)

        delta = math.pow(b, 2) - 4 * a * c

        if delta < 0:
            return math.inf

        t1 = (-b + math.sqrt(delta)) / (2 * a)

        t2 = (-b - math.sqrt(delta)) / (2 * a)

        return min(t1, t2)
        # return (t1, t2)

    def calculate_normal(self, p_i: Vector):
        return (p_i - self.center) / self.radius
