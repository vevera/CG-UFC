from vector import Vector
import math


def scale(alfa, vector: Vector):
    new_vector = []

    for element in vector.elements:
        new_vector.append(alfa * element)

    return Vector(new_vector)


def divide_by_value(vector: Vector, alfa):
    new_vector = []

    for element in vector.elements:
        new_vector.append(element / alfa)

    return Vector(new_vector)


def product(vector1: Vector, vector2: Vector):
    # print("pro")
    if vector1.length != vector2.length:
        return

    result = 0
    for i in range(vector1.length):

        result += vector1.get(i) * vector2.get(i)

    return result


def product_2(vector1: Vector, vector2: Vector):
    new_vector = []

    if vector1.length != vector2.length:
        return

    for i in range(vector1.length):
        new_vector.append(vector1.get(i) * vector2.get(i))

    return Vector(new_vector)


def minus(vector1: Vector, vector2: Vector):
    # print("min")
    if vector1.length != vector2.length:
        return

    new_vector = []
    for i in range(vector1.length):

        new_vector.append(vector1.get(i) - vector2.get(i))

    return Vector(new_vector)


def sum(vector1: Vector, vector2: Vector):
    # print("sum")
    if vector1.length != vector2.length:
        return

    new_vector = []
    for i in range(vector1.length):

        new_vector.append(vector1.get(i) + vector2.get(i))

    return Vector(new_vector)


def length(vector: Vector):
    vector_len = product(vector, vector)
    return math.sqrt(vector_len)


def normalize(vector: Vector):

    vector_len = length(vector)
    return vector / vector_len
