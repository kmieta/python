import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        xStr = str(self.x)
        yStr = str(self.y)
        return f"({xStr}, {yStr})"

    def __repr__(self):         # zwraca string "Point(x, y)"
        xStr = str(self.x)
        yStr = str(self.y)
        return f"Point({xStr}, {yStr})"

    def __eq__(self, other):    # obsługa point1 == point2
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y 
        else: 
            return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        if not isinstance(other, Point):
            raise TypeError
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # v1 - v2
        if not isinstance(other, Point):
            raise TypeError
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny, zwraca liczbę
        if not isinstance(other, Point):
            raise TypeError
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        if not isinstance(other, Point):
            raise TypeError
        return self.x * other.y - self.y * other.x

    def length(self): 
        return math.sqrt(self.x**2 + self.y**2)         # długość wektora

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 
    
    def setUp(self):
        self.point67 = Point(6, 7)
        self.point6767 = Point(6, 7)
        self.point12 = Point(1, 2)

    def test_str(self):
        self.assertEqual(str(self.point67), '(6, 7)')
        self.assertEqual(str(self.point12), '(1, 2)')

    def test_repr(self):
        self.assertEqual(repr(self.point67), 'Point(6, 7)')
        self.assertEqual(repr(self.point12), 'Point(1, 2)')

    def test_eq(self):
        self.assertTrue(self.point67 == self.point6767)
        self.assertFalse(self.point67 == self.point12)

    def test_ne(self):
        self.assertFalse(self.point67 != self.point6767)
        self.assertTrue(self.point67 != self.point12)

    def test_add(self):
        self.assertEqual(self.point67 + self.point12, Point(7, 9))
        self.assertEqual(self.point67 + self.point67, Point(12, 14))
        self.assertEqual(self.point12 + self.point12, Point(2, 4))

    def test_sub(self):
        self.assertEqual(self.point67 - self.point12, Point(5, 5))
        self.assertEqual(self.point12 - self.point67, Point(-5, -5))
        self.assertEqual(self.point67 - self.point67, Point(0, 0))
        self.assertEqual(self.point12 - self.point12, Point(0, 0))

    def test_mul(self):
        self.assertEqual(self.point67 * self.point12, 20)
        self.assertEqual(self.point67 * self.point67, 85)
        self.assertEqual(self.point12 * self.point12, 5)

    def test_cross(self):
        self.assertEqual(self.point67.cross(self.point12), 5)
        self.assertEqual(self.point67.cross(self.point67), 0)

    def test_length(self):
        self.assertEqual(self.point67.length(), math.sqrt(85))
        self.assertEqual(self.point12.length(), math.sqrt(5))


if __name__ == '__main__':
    unittest.main()
