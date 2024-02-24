#!/usr/bin/python3
# test_square.py
# Rachid BOULMANI
"""
defines unittests for square.py
"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Square class.
    """

    def test_square_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_square_is_Rectangle(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_arg(self):
        """Tests Square with No arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Tests Square with one argument"""
        r1 = Square(10)
        r2 = Square(10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_two_arg(self):
        """Tests Square with two arguments"""
        r1 = Square(10, 2)
        r2 = Square(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_arg(self):
        """Tests Square with three arguments"""
        r1 = Square(10, 2, 0)
        r2 = Square(2, 10, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_all_arg(self):
        """Tests Square with all arguments"""
        r1 = Square(10, 2, 0, 0)
        r2 = Square(2, 10, 1, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_more_arg(self):
        """Tests Square with more arguments"""
        with self.assertRaises(TypeError):
            Square(2, 10, 0, 0, 12, 1)


class TestSquareStr(unittest.TestCase):
    """Unittests for testing the string method of Square class."""

    @staticmethod
    def capture_stdout(square):
        """Captures and returns text printed to stdout."""
        capture = io.StringIO()
        sys.stdout = capture
        print(square)
        sys.stdout = sys.__stdout__
        return capture

    def test_str_width_height(self):
        """Tests __str__ with width and height"""
        s = Square(4)
        capture = TestSquareStr.capture_stdout(s)
        text = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(text, capture.getvalue())

    def test_str_width_height_x(self):
        """Tests __str__ with width, height and x"""
        s = Square(4, 2)
        capture = TestSquareStr.capture_stdout(s)
        text = "[Square] ({}) 2/0 - 4\n".format(s.id)
        self.assertEqual(text, capture.getvalue())

    def test_str_width_height_x_y(self):
        """Tests __str__ with width, height x, and y"""
        s = Square(4, 2, 1)
        capture = TestSquareStr.capture_stdout(s)
        text = "[Square] ({}) 2/1 - 4\n".format(s.id)
        self.assertEqual(text, capture.getvalue())

    def test_str_method_changed_attributes(self):
        """Tests __str__ after attributes update"""
        s = Square(4, 2, 1)
        s.width = 12
        s.height = 12
        s.x = 13
        s.y = 14
        capture = TestSquareStr.capture_stdout(s)
        text = "[Square] ({}) 13/14 - 12\n".format(s.id)
        self.assertEqual(text, capture.getvalue())

    def test_str_with_arg(self):
        """Tests __str__ with arguments"""
        s = Square(4, 2, 1)
        with self.assertRaises(TypeError):
            s.__str__(0)


if __name__ == "__main__":
    unittest.main()
