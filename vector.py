class Vector:
    def __init__(self, elements):

        self.length = len(elements)
        self.elements = elements

    def get(self, index):
        return self.elements[index]

    def __add__(self, vector):
        # print("sum")
        if self.length != vector.length:
            return

        new_vector = []
        for i in range(self.length):

            new_vector.append(self.get(i) + vector.get(i))

        return Vector(new_vector)

    def __sub__(self, vector):
        # print("sum")
        if self.length != vector.length:
            return

        new_vector = []
        for i in range(self.length):

            new_vector.append(self.get(i) - vector.get(i))

        return Vector(new_vector)

    def __mul__(self, vector):
        if self.length != vector.length:
            return

        result = 0
        for i in range(self.length):

            result += self.get(i) * vector.get(i)

        return result

    def __truediv__(self, value):

        new_vector = []
        for i in range(self.length):

            new_vector.append(self.get(i) / value)

        return Vector(new_vector)

    def __and__(self, vector):
        new_vector = []

        if self.length != vector.length:
            return

        for i in range(self.length):
            new_vector.append(self.get(i) * vector.get(i))

        return Vector(new_vector)
