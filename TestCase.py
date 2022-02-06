#!/usr/bin/python3
import sys
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

    def test_area_neg(self):

        with self.assertRaises(ValueError):
            p1 = Rectangle(-5, -5)
            p1.area()

    def test_area_zero(self):

        with self.assertRaises(ValueError):
            p1 = Rectangle(0, 0)
            p1.area()

    def test_area_bool(self):

        with self.assertRaises(TypeError):
            R = Rectangle(True, True)
            R.area()

    def test_area_str(self):

        with self.assertRaises(TypeError):
            R = Rectangle("Alfred", "Robin")
            R.area()

    def test_area_tuple(self):

        with self.assertRaises(TypeError):
            R = Rectangle((1, 2, 3), (1, 2, 3))
            R.area()

    def test_area_list(self):

        with self.assertRaises(TypeError):
            R = Rectangle([1, 2, 3], [1, 2, 3])
            R.area()

    def test_area_dict(self):

        with self.assertRaises(TypeError):
            R = Rectangle({1, 2, 3}, {1, 2, 3})
            R.area()

    def test_area_float(self):

        with self.assertRaises(TypeError):
            R = Rectangle(float("inf"), 7)
            R.area()
        with self.assertRaises(TypeError):
            R = Rectangle(float("NaN"), 7)
            R.area()

    def test_area_empty(self):
        with self.assertRaises(TypeError):
            R = Rectangle()
            R.area()

    def test_area_None(self):
        with self.assertRaises(TypeError):
            R = Rectangle(None, None)
            R.area()


class Test_display(unittest.TestCase):

    def test_display(self):
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

        R = Rectangle(2, 2, 3, 4)
        self.assertEqual(R.display(), None)

    def test_display_neg(self):
        with self.assertRaises(ValueError):
            R = Rectangle(-5, -5, -5, -5)
            R.display()

    def test_display_zero(self):
        with self.assertRaises(ValueError):
            R = Rectangle(0, 0, 0, 0)
            R.display()

    def test_display_bool(self):
        with self.assertRaises(TypeError):
            R = Rectangle(True, False, False, True)
            R.display()

    def test_display_str(self):
        with self.assertRaises(TypeError):
            R = Rectangle("Alfred", "Robin", "Batman", "Batgirl")
            R.display()

    def test_display_tuple(self):
        with self.assertRaises(TypeError):
            R = Rectangle((1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3))
            R.display()

    def test_display_list(self):
        with self.assertRaises(TypeError):
            R = Rectangle([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3])
            R.display()

    def test_display_dict(self):
        with self.assertRaises(TypeError):
            R = Rectangle({1, 2, 3}, {1, 2, 3},
                          {1, 2, 3}, {1, 2, 3})
            R.display()

    def test_display_float_inf(self):
        with self.assertRaises(TypeError):
            R = Rectangle(float("inf"), float("inf"),
                          float("inf"), float("inf"))
            R.display()

    def test_display_float_NaN(self):
        with self.assertRaises(TypeError):
            R = Rectangle(float("NaN"), float("NaN"),
                          float("NaN"), float("NaN"))
            R.display()

    def test_display_empty(self):
        with self.assertRaises(TypeError):
            R = Rectangle()
            R.display()

    def test_display_None(self):
        with self.assertRaises(TypeError):
            R = Rectangle(None, None, None, None)
            R.display()


class Test_width(unittest.TestCase):

    def test_width(self):
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
        R = Rectangle(5, 5, 2, 3)
        self.assertEqual(R.width, 5)

    def test_width_neg(self):
        with self.assertRaises(ValueError):
            R = Rectangle(-5, -5, -5, -5)
            R.width()

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            R = Rectangle(0, -5, -5, -5)
            R.width()

    def test_width_bool(self):
        with self.assertRaises(TypeError):
            R = Rectangle(True, False, False, True)
            R.width()

    def test_width_str(self):
        with self.assertRaises(TypeError):
            R = Rectangle("Alfred", "Robin", "Batman", "Batgirl")
            R.width()

    def test_width_tuple(self):
        with self.assertRaises(TypeError):
            R = Rectangle((1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3))
            R.width()

    def test_width_list(self):
        with self.assertRaises(TypeError):
            R = Rectangle([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3])
            R.width()

    def test_width_dict(self):
        with self.assertRaises(TypeError):
            R = Rectangle({1, 2, 3}, {1, 2, 3}, {1, 2, 3}, {1, 2, 3})
            R.width()

    def test_width_float_inf(self):
        with self.assertRaises(TypeError):
            R = Rectangle(float("inf"), float("inf"),
                          float("inf"), float("inf"))
            R.width()

    def test_width_float_NaN(self):
        with self.assertRaises(TypeError):
            R = Rectangle(float("NaN"), float("NaN"),
                          float("NaN"), float("NaN"))
            R.width()

    def test_width_empty(self):
        with self.assertRaises(TypeError):
            R = Rectangle()
            R.width()

    def test_width_None(self):
        with self.assertRaises(TypeError):
            R = Rectangle(None, None, None, None)
            R.width()


class Test_height(unittest.TestCase):

    def test_height(self):
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
        R = Rectangle(5, 5, 2, 3)
        self.assertEqual(R.height, 5)

    def test_height_neg(self):

        with self.assertRaises(ValueError):
            R = Rectangle(-5, -5, -5, -5)
            R.height()

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            R = Rectangle(-5, 0, -5, -5)
            R.height()

    def test_height_bool(self):
        with self.assertRaises(TypeError):
            R = Rectangle(True, False, False, True)
            R.height()

    def test_height_str(self):
        with self.assertRaises(TypeError):
            R = Rectangle("Alfred", "Robin", "Batman", "Batgirl")
            R.height()

    def test_height_tuple(self):
        with self.assertRaises(TypeError):
            R = Rectangle((1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3))
            R.height()

    def test_height_list(self):
        with self.assertRaises(TypeError):
            R = Rectangle([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3])
            R.height()

    def test_height_dict(self):
        with self.assertRaises(TypeError):
            R = Rectangle({1, 2, 3}, {1, 2, 3}, {1, 2, 3}, {1, 2, 3})
            R.height()

    def test_height_float_inf(self):
        with self.assertRaises(TypeError):
            R = Rectangle(float("inf"), float("inf"),
                          float("inf"), float("inf"))
            R.height()

    def test_height_flaot_NaN(self):
        with self.assertRaises(TypeError):
            R = Rectangle(float("NaN"), float("NaN"),
                          float("NaN"), float("NaN"))
            R.height()

    def test_height_empty(self):
        with self.assertRaises(TypeError):
            R = Rectangle()
            R.height()

    def test_height_None(self):
        with self.assertRaises(TypeError):
            R = Rectangle(None, None, None, None)
            R.height()


if __name__ == "__main__":
    unittest.main()
