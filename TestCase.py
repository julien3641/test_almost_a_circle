#!/usr/bin/python3
import unittest

from models.base import Base
from models.rectangle import Rectangle

class Test_Area(unittest.TestCase):

    def test_is_num(self):
        """Test with number"""
        p1 = Rectangle(2, 3)
        self.assertEqual(p1.area(), 6)

if __name__ == "__main__":
    unittest.main()
