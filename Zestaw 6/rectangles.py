from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1.x, self.pt1.y}, {self.pt2.x, self.pt2.y}]'

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle{self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y}'

    def __eq__(self, other):    # obsługa rect1 == rect2
        if isinstance(other, Rectangle):
            return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta (Point)
        return Point((self.pt1.x + self.pt2.x)/2 , (self.pt1.y + self.pt2.y)/2)
    
    def area(self):             # pole powierzchni (liczba)
        a = abs(self.pt2.y - self.pt1.y)
        b = abs(self.pt2.x - self.pt1.x)
        return a * b

    def move(self, x, y):       # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
 
# Kod testujący moduł.

import unittest


class TestRectangle(unittest.TestCase): 

    def setUp(self):
        self.rectangle12 = Rectangle(1, 2, 3, 4)
        self.rectangle1212 = Rectangle(1, 2, 3, 4)
        self.rectangle24 = Rectangle(2, 2, 4, 4)
        self.rectangle36 = Rectangle(3, 3, 6, 6)

    def test_str(self):
       self.assertEqual(str(self.rectangle12), "[(1, 2), (3, 4)]")
       self.assertEqual(str(self.rectangle24), "[(2, 2), (4, 4)]")
       self.assertEqual(str(self.rectangle36), "[(3, 3), (6, 6)]")

    
    def test_repr(self):
        self.assertEqual(repr(self.rectangle12), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(self.rectangle24), "Rectangle(2, 2, 4, 4)")
        self.assertEqual(repr(self.rectangle36), "Rectangle(3, 3, 6, 6)")

    def test_eq(self):
       self.assertTrue(self.rectangle12 == self.rectangle1212)
       self.assertFalse(self.rectangle12 == self.rectangle24)
       self.assertFalse(self.rectangle24 == self.rectangle36)

    def test_ne(self):
       self.assertFalse(self.rectangle12 != self.rectangle1212)
       self.assertTrue(self.rectangle24 != self.rectangle36)
       self.assertTrue(self.rectangle24 != self.rectangle12)

    def test_center(self):
       self.assertTrue(self.rectangle12.center() == Point(2, 3))
       self.assertTrue(self.rectangle24.center() == Point(3, 3))

    def test_area(self):
       self.assertEqual(self.rectangle24.area(), 4)
       self.assertEqual(self.rectangle36.area(), 9)
       self.assertEqual(self.rectangle12.area(), 4)

    def test_move(self):
        self.rectangle12.move(1, 1)
        self.assertTrue(self.rectangle12 == Rectangle(2 ,3 ,4 ,5))
        self.setUp()
        self.rectangle24.move(2, 2)
        self.assertTrue(self.rectangle24 == Rectangle(4 ,4 ,6 ,6))
        self.setUp()


if __name__ == '__main__':
    unittest.main()