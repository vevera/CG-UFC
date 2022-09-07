from camera import Camera
from vector import Vector
from traceray import TraceRay
from utils import minus
from canvas import Canvas
from light import Light
from shapes.shape import Shape
from typing import List
import math


class Scene:
    def __init__(
        self, elements: List[Shape], canvas: Canvas, light: Light, ambient_light: Light
    ):

        self.elements = elements
        self.canvas = canvas
        self.light = light
        self.ambient_light = ambient_light

    def take_a_picture(self, camera: Camera, view_port, bgColor):

        dx = view_port[0] / self.canvas.n_column
        dy = view_port[1] / self.canvas.n_rows
        for l in range(self.canvas.n_rows):
            yj = view_port[1] / 2 - dy / 2 - l * dy
            for c in range(self.canvas.n_column):
                xj = -view_port[0] / 2 + dx / 2 + c * dx

                dr = minus(Vector([xj, yj, view_port[2]]), camera.initial_position)
                cor = TraceRay(
                    camera.initial_position,
                    dr,
                    view_port[2],
                    math.inf,
                    self.elements,
                    bgColor,
                    self.light,
                    self.ambient_light,
                )

                self.canvas.paintASquare(l, c, cor)

        self.canvas.show()
