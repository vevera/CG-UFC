from vector import Vector
from reflexivity import Reflexivity


class Shape:
    def __init__(self, reflexivity: Reflexivity, color=(0, 0, 0)):
        self.color = color
        self.reflexivity = reflexivity

    def intersect(self, p0: Vector, dr: Vector):
        pass

    def calculate_normal(self, p_i: Vector):
        pass
