from vector import Vector
from utils import scale, product, minus
import math


class Light:

    def __init__(self, intensity: Vector, position: Vector):
        self.intensity = intensity
        self.position = position