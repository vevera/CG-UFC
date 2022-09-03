from typing import List
from shape import Shape
from sphere import Sphere
from vector import Vector
from light import Light
from utils import *
import math


def TraceRay(p0:Vector, dr:Vector, t_min:float, t_max:float, shapes: List[Shape], bgColor, light:Light):
    closest_t = math.inf
    closest_shape = None
    for shape in shapes:
        t1, t2 = shape.intersect(p0, dr)
        if ((t1 >= t_min) and (t1 <= t_max)) and (t1 < closest_t):
            closest_t = t1
            closest_shape = shape
        if ((t2 >= t_min) and (t2 <= t_max)) and (t2 < closest_t):
            closest_t = t2
            closest_shape = shape
    if closest_shape == None:
        return bgColor

    #VAI MUDAR PRA CADA SHAPE
    # Calculo do ponto de intersecção com a esfera
    P_i = p0 + scale(closest_t, dr) # dr = (D - O)

    # vetores unitários usados no modelo
    normal = (P_i - closest_shape.center) / closest_shape.radius
    #lr = divide_by_value(minus(Vector(light.position), P_i),product(minus(Vector(light.position), P_i),minus(Vector(light.position), P_i)))
    lr = normalize(Vector(light.position) - P_i)
    v = normalize(scale(-1,dr))

    # reflexão difusa

    K = Vector([1,1,1])
    Ke = Vector([0.6,0.6,0.6])

    I_d =scale(max(lr * normal, 0), product_2(Vector(light.intensity),K))

    # reflexão especular

    #I_e = (I_F@K)*(v . r)^m
    r = scale(2, scale(lr * normal, normal)) - lr
    I_e = scale(v * r, product_2(Vector(light.intensity),Ke))

    # Intensidade que chega no olho do observador
    Ieye = I_d + I_e

    R = int(closest_shape.color[0]*Ieye.get(0))
    B = int(closest_shape.color[1]*Ieye.get(1))
    G = int(closest_shape.color[2]*Ieye.get(2))

    return (R, G, B)