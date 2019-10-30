"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""


class Vector:
    # dim stands for dimension
    @property
    def dim(self):
        return self._dim

    @dim.setter
    def dim(self, dim):
        self._dim = dim

    @property
    def len(self):
        return self._len

    @len.setter
    def len(self, len):
        self._len = len

    def __init__(self, *args):
        self.dim = len(args)
        self.components = list(args)
        self.len = sum(list(map(lambda x: x ** 2, self.components))) ** 0.5

    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        return tuple(map(lambda x, y: y - x, beg, end))

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        return Vector(*list(map(lambda x, y: y - x, beg, end)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if other.dim == self.dim:
                return all(list(map(lambda x, y: x == y, self.components, other.components)))
            else:
                raise Exception
        else:
            raise NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if other.dim == self.dim:
                return Vector(*list(map(lambda x, y: x + y, self.components, other.components)))
            else:
                raise Exception
        else:
            raise NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if other.dim == self.dim:
                return Vector(*list(map(lambda x, y: x - y, self.components, other.components)))
            else:
                raise Exception
        else:
            raise NotImplemented

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            if other.dim == self.dim:
                return sum(list(map(lambda x, y: x * y, self.components, other.components)))
            else:
                raise Exception
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*list(map(lambda x: x * other, self.components)))
        else:
            raise NotImplemented

    def __len__(self):
        return self.dim


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 2
    assert Vector(3,4).dim == 2
    assert Vector(3,4).len == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
