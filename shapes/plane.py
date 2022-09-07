from reflexivity import Reflexivity
from shapes.shape import Shape
from vector import Vector
from utils import scale, product, minus
import math


class Plane(Shape):
    def __init__(self, p_pi: Vector, n: Vector, color, reflexivity: Reflexivity):
        super().__init__(reflexivity, color)
        self.p_pi = p_pi
        self.n = n

    def intersect(self, p0: Vector, dr: Vector):

        t: float

        w = p0 - self.p_pi

        denominator = dr * self.n
        # print("denominador: ", denominator)
        if denominator == 0:
            return math.inf

        t = (scale(-1, w) * self.n) / denominator

        return t

    def calculate_normal(self, p_i: Vector):
        return self.n
