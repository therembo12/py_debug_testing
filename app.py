import math
import pytest

# function for finding roots


def quadratic_equation(a, b, c):

    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        x1 = ((-b + sqrt_val)/(2 * a))
        x2 = ((-b - sqrt_val)/(2 * a))
        return x1, x2
    elif dis == 0:
        print(" real and same roots")
        y0 = (-b / (2 * a))
        return y0
    # when discriminant is less than 0
    else:
        print("Complex Roots")
        return None


class TestQuadraticEquation:
    def test1(self):
        assert quadratic_equation(2, 1, -1) == (0.5, -1.0)

    def test2(self):
        assert quadratic_equation(1, -4, 4) == (2.0)

    def test3(self):
        assert quadratic_equation(4, 1, 2) == None
