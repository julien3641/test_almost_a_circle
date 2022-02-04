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
    def work_tests(self):
        """
        Tests about:
            - positive integers
            - negative integers
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
