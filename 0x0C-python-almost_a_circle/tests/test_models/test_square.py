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


class TestSquareSize(unittest.TestCase):
    """Unittests for testing the size attribute."""

    def test_None_size(self):
        """Tests size attribute with None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        """Tests size attribute with a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        """Tests size attribute with a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.1)

    def test_complex_size(self):
        """Tests size attribute with a complex"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(1))

    def test_dict_size(self):
        """Tests size attribute with a dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 1})

    def test_bool_size(self):
        """Tests size attribute with a boolean"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_list_size(self):
        """Tests size attribute with a list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        """Tests size attribute with a set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3})

    def test_tuple_size(self):
        """Tests size attribute with a tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3))

    def test_frozenset_size(self):
        """Tests size attribute with a frozen set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 2, 1}))

    def test_range_size(self):
        """Tests size attribute with a range"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(1))

    def test_bytes_size(self):
        """Tests size attribute with bytes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        """Tests size attribute with a byte array"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'Python'))

    def test_memoryview_size(self):
        """Tests size attribute with a memory view"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'Python'))

    def test_inf_size(self):
        """Tests size attribute with Inf"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        """Tests size attribute with NaN"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative_size(self):
        """Tests size attribute with a negative value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_zero_size(self):
        """Tests size attribute with 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)


if __name__ == "__main__":
    unittest.main()
