#!/usr/bin/python3
"""
Add unit test for the class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    This class test the class Base.
    """
    def tests_instance(self):
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
        b = Base(1)
        self.assertEqual(b.id, 1)
        b = Base(12)
        self.assertEqual(b.id, 12)
        b = Base(201)
        self.assertEqual(b.id, 201)

        b = Base(-1)
        self.assertEqual(b.id, -1)
        b = Base(-12)
        self.assertEqual(b.id, -12)

        b = Base(True)
        self.assertEqual(b.id, True)

        b = Base('hello')
        self.assertEqual(b.id, 'hello')

        b = Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))
        b = Base({1, 2, 3})
        self.assertEqual(b.id, {1, 2, 3})
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base({'name': 'holberton', 'age': 6})
        self.assertEqual(b.id, {'name': 'holberton', 'age': 6})

        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)

        """
        TESTS EXCEPTIONS:
            - more than one argument
        """
        with self.assertRaises(TypeError):
            Base(1, 1)


    def tests_to_json_string(self):

    def tests_save_to_file(self):

    def tests_from_json_string(self):

    def tests_create_instance(self):

    def load_from_file(self):

