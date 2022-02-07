#!/usr/bin/python3
"""This is the square.py unittest module for task 12 and 14"""


from unittest import TestCase, mock
from io import StringIO

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square_update_with_kwargs(TestCase):
    """Test cases for Square's update with **kwargs method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_kwargs_id(self):
        s = Square(2, 1, 2, 42)
        s.update(id=24)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 2")

    def test_update_kwargs_id_size(self):
        s = Square(2, 1, 2, 42)
        s.update(size=10, id=24)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 10")

    def test_update_kwargs_id_size_x(self):
        s = Square(2, 1, 2, 42)
        s.update(size=10, id=24, x=30)
        self.assertEqual(str(s), "[Square] (24) 30/2 - 10")

    def test_update_kwargs_id_size_x_y(self):
        s = Square(2, 1, 2, 42)
        s.update(y=40, size=10, id=24, x=30)
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def test_update_kwargs_too_many_args(self):
        s = Square(2, 1, 2, 42)
        s.update(y=40, size=10, id=24, x=30, betty="holberton")
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def test_update_kwargs_mixed_too_many_args(self):
        s = Square(2, 1, 2, 42)
        s.update(y=40, size=10, betty="holberton", id=24, x=30)
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def test_update_kwargs_args_before(self):
        s = Square(2, 1, 2, 42)
        s.update(42, 42, y=10, x=30)
        self.assertEqual(str(s), "[Square] (42) 1/2 - 42")

    def test_update_kwargs_not_all_mixed(self):
        s = Square(2, 1, 2, 42)
        s.update(y=10, x=10, size=10)
        self.assertEqual(str(s), "[Square] (42) 10/10 - 10")

    def test_update_kwargs_only_wrong_keys(self):
        s = Square(2, 1, 2, 42)
        s.update(betty="holberton", holberton="betty")
        self.assertEqual(str(s), "[Square] (42) 1/2 - 2")


class Test_Square_to_dict(TestCase):
    """Test cases for Square's to_dictionary method."""

    def test_to_dictionary_basic(self):
        s = Square(2, 1, 2, 42)
        expected = {'size': 2, 'x': 1, 'y': 2, 'id': 42}
        self.assertDictEqual(s.to_dictionary(), expected)

    def test_to_dictionary_basic_with_args(self):
        with self.assertRaises(TypeError):
            Square(2, 1, 2, 42).to_dictionary(42)


if __name__ == "__main__":
    unittest.main()
