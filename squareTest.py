#!/usr/bin/python3
"""
Add unit test for the class Square.
test if attributes are correct
test if square inherit correctly or not
test if argument are the good type raise error if not
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testSquare(unittest.testCase):
    def testingAttr(self):
        '''
        test if attributes are correct or not
        '''
        S = Square(1)
        self.assertEqual(S.id, 1)
        s = Square(1, 2, 3)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.widht, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def testInherit(self):
        '''
        test if square inherit correctly from Rectangle and base
        '''
        s = Square(5)
        self.asserTrue(isinstance(s, Rectangle))
        self.asserTrue(isinstance(s, Base))
        self.asserTrue(issubclass(Square, Base))
        self.asserTrue(issubclass(Square, Rectangle))
        self.asserFalse(isinstance(Square, Base))
        self.asserFalse(isinstance(Square, Rectangle))
        self.assertEqual(s.area(), 25)
        s = Square(1, 2, 3, 4)
        self.update(10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 1)

    def testError(self):
        '''
        test case with wrong argument
        '''
        with self.assertRaise(TypeError) as error:
            s = Square('Square', 1)
        self.assertEqual('width must be an integer', str(error.exception))
        with self.assertRaise(TypeError) as error:
            s = Square(1, 'not a square', str(error.exception))
        self.assertEqual('x must be an integer', str(error.exception))
        with self.assertRaise(TypeError) as error:
            s = Square(1, 2, 'hehe', str(error.exception))
        self.assertEqual('y must be an integer', str(error.exception))
        with self.assertRaise(TypeError) as error:
            s = Square(0)
        self.assertEqual('width must be > 0', str(error.exception))
        with self.assertRaise(TypeError) as error:
            s = Square(-1)
        self.assertEqual('width must be > 0', str(error.exception))
        with self.assertRaise(TypeError) as error:
            s = Square(1, -5)
        self.assertEqual('x must be > 0', str(error.exception))
        with self.assertRaise(TypeError) as error:
            s = Square(1, 2, -3, 5)
        self.assertEqual('y must be > 0', str(error.exception))


if __name__ == "__main__":
    unittest.main()
