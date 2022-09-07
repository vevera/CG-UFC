from vector import Vector


class Light:
    def __init__(self, intensity: Vector, position: Vector, type: str = "point"):
        self.intensity = intensity
        self.position = position
        self.type = type
