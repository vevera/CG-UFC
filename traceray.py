from typing import List
from shapes.shape import Shape
from vector import Vector
from light import Light
from utils import *
import math


def TraceRay(
    p0: Vector,
    dr: Vector,
    t_min: float,
    t_max: float,
    shapes: List[Shape],
    bgColor,
    light: Light,
    ambient_light: Light,
):
    closest_t = math.inf
    closest_shape = None
    for shape in shapes:
        t = shape.intersect(p0, dr)
        if t > 0 and ((t >= t_min) and (t <= t_max)) and (t < closest_t):
            closest_t = t
            closest_shape = shape
    if closest_shape == None:
        return bgColor

    # Calculo do ponto de intersecção com a esfera
    P_i = p0 + scale(closest_t, dr)  # dr = (D - O)

    # vetores unitários usados no modelo
    normal = closest_shape.calculate_normal(P_i)
    lr = normalize(light.position - P_i)
    v = normalize(scale(-1, dr))
    r = scale(2, scale(lr * normal, normal)) - lr

    zero_intensity_light: Light = Light(Vector([0, 0, 0]), light.position)

    light_blocked = light_being_blocked(closest_shape, shapes, P_i, light, lr)

    color = calculate_light_intensity(
        light if not light_blocked else zero_intensity_light,
        normal,
        lr,
        v,
        r,
        closest_shape,
        ambient_light,
    )

    return color


def calculate_light_intensity(
    light: Light,
    n: Vector,
    l: Vector,
    v: Vector,
    r: Vector,
    object: Shape,
    ambient_light: Light,
):
    Kd = object.reflexivity.kd
    Ke = object.reflexivity.ke
    Ka = object.reflexivity.ka
    m = object.reflexivity.m
    color = object.color

    # reflexão difusa
    I_d = scale(max(l * n, 0), product_2(light.intensity, Kd))

    # reflexão especular
    I_e = scale(math.pow(v * r, m), product_2(light.intensity, Ke))

    # reflexão ambiente
    I_a = product_2(ambient_light.intensity, Ka)

    # Intensidade que chega no olho do observado
    Ieye = I_d + I_e + I_a

    R = int(color[0] * Ieye.get(0))
    G = int(color[1] * Ieye.get(1))
    B = int(color[2] * Ieye.get(2))

    return (R, G, B)


def light_being_blocked(
    closest_shape: Shape, shapes: Shape, P_i: Vector, light: Light, lr: Vector
):

    for shape in shapes:
        if shape != closest_shape:
            s = shape.intersect(P_i, lr)
            vec = light.position - P_i
            vector_len = length(vec)
            if s >= 0 and s < vector_len:
                # Esse if corrige o erro para quando o centro da luz pertence ao plano
                if abs(s - vector_len) > 0.000000001:
                    return True

    return False
