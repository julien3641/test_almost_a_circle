#!/usr/bin/python3
import unittest

from models.base import Base
from models.rectangle import Rectangle

class Test_Area(unittest.TestCase):

    def test_area(self):
        """
        Tests about:
            - positive integers
            - negative integers
            - boolean
            - string
            - tuple
            - set
            - list
            - empty
            - None
        """
        p1 = Rectangle(2, 3)
        self.assertEqual(p1.area(), 6)

        with self.assertRaises(ValueError):
            p1 = Rectangle(-5, -5)
            p1.area()

        with self.assertRaises(TypeError):
            R = Rectangle(True, True)
            R.area()

        with self.assertRaises(TypeError):
            R = Rectangle("Alfred", "Robin")
            R.area()

        with self.assertRaises(TypeError):
            R = Rectangle((1, 2, 3), (1, 2, 3))
            R.area()

        with self.assertRaises(TypeError):
            R = Rectangle([1, 2, 3], [1, 2, 3])
            R.area()

        with self.assertRaises(TypeError):
            R = Rectangle({1, 2, 3}, {1, 2, 3})
            R.area()
        with self.assertRaises(TypeError):
            R = Rectangle(float("inf"), 7)
            R.area()
        with self.assertRaises(TypeError):
            R = Rectangle(float("NaN"), 7)
            R.area()

        with self.assertRaises(TypeError):
            R = Rectangle()
            R.area()
        with self.assertRaises(TypeError):
            R = Rectangle(None, None)
            R.area()

class Test_display(unittest.TestCase):

    def test_display(self):
        """Test with number, +, - , bool, str, tuple, set
        list, empty and None"""


       with self.assertRaises(TypeError):
            p1 = Rectangle(-5, -5)
            p1.display()

if __name__ == "__main__":
    unittest.main()
