import math
import pytest


class Triangle:

    def __init__(self, data):
        if len(data) != 3 or type(data) != tuple or type(data[0]) != int or type(data[1]) != int or type(data[2]) != int:
            raise TriangleNotValidArgumentException
        else:
            self.a = data[0]
            self.b = data[1]
            self.c = data[2]

    def get_area(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a and self.a > 0 and self.b > 0 and self.c > 0:
            P = (self.a + self.b + self.c) / 2
            S = int(math.sqrt(P * (P-self.a)*(P-self.b)*(P-self.c)))
            return S
        else:
            raise TriangleNotExistException


class TriangleNotExistException(Exception):
    print('Can`t create triangle with this arguments')


class TriangleNotValidArgumentException(Exception):
    print('Not valid arguments')


data = [
    ((3, 4, 5), 6.0),
    ((10, 10, 10), 43.30),
    ((6, 7, 8), 20.33),
    ((7, 7, 7), 21.21),
    ((50, 50, 75), 1240.19),
    ((37, 43, 22), 406.99),
    ((26, 25, 3), 36.0),
    ((30, 29, 5), 72.0),
    ((87, 55, 34), 396.0),
    ((120, 109, 13), 396.0),
    ((123, 122, 5), 300.0)
]
not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]

not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    10
]


class TestTria:

    def test1(self):

        for item in data:
            assert Triangle(item[0]).get_area() == int(item[1])

    def test2(self):
        with pytest.raises(TriangleNotExistException) as e:
            for item in not_valid_triangle:
                assert Triangle(item).get_area()

    def test3(self):
        with pytest.raises(TriangleNotValidArgumentException) as e:
            for item in not_valid_arguments:
                assert Triangle(item).get_area()
