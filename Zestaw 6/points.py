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
        return self.x * self.y + other.x * other.y

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

class TestPoint(unittest.TestCase): pass