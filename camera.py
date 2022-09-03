from vector import Vector
from traceray import TraceRay
from PIL import Image
from utils import minus
import math
from sphere import Sphere

class Camera:
    
    def __init__(self, initial_positon : Vector):
        self.initial_position = initial_positon
        

    
    