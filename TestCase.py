#!/usr/bin/python3
import unittest

from models.base import Base
from models.rectangle import Rectangle

class Test_Area(unittest.TestCase):

    def test_area(self):
        """Test with number, +, - , bool, str, tuple, set
        list, empty and None"""

        p1 = Rectangle(2, 3)
        self.assertEqual(p1.area(), 6)

        with self.assertRaises(ValueError):
            p1 = Rectangle(-5, -5)
            p1.area()

        with self.assertRaises(TypeError):
            Rectangle(True, True)

        with self.assertRaises(TypeError):
            Rectangle("Alfred", "Robin")

        with self.assertRaises(TypeError):
            Rectangle((1, 2, 3), (1, 2, 3))

        with self.assertRaises(TypeError):
            Rectangle([1, 2, 3], [1, 2, 3])

        with self.assertRaises(TypeError):
            Rectangle({1, 2, 3}, {1, 2, 3})

        with self.assertRaises(TypeError):
            Rectangle(float("inf"), 7)

        with self.assertRaises(TypeError):
            Rectangle(float("NaN"), 7)

        with self.assertRaises(TypeError):
                Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(None, None)

class Test_display(unittest.TestCase):

    def test_display(self):
        """Test with number, +, - , bool, str, tuple, set
        list, empty and None"""

            display = "\n\n\n\n   ##\n   ##\n"
            o = self.out_c()
            self.assertEqual(o, display)

       with self.assertRaises(ValueError):
            p1 = Rectangle(-5, -5)
            p1.display()

if __name__ == "__main__":
    unittest.main()
