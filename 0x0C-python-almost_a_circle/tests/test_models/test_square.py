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


class TestSquareUpdate(unittest.TestCase):
    """Unittests for testing update method of the Square class."""

    # Test args
    def test_update_args_zero(self):
        """Tests Update with no arguments"""
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        """Tests Update with one argument"""
        s = Square(10, 10, 10, 10)
        s.update(99)
        self.assertEqual("[Square] (99) 10/10 - 10", str(s))

    def test_update_args_two(self):
        """Tests Update with two arguments"""
        s = Square(10, 10, 10, 10)
        s.update(99, 1)
        self.assertEqual("[Square] (99) 10/10 - 1", str(s))

    def test_update_args_three(self):
        """Tests Update with two arguments"""
        s = Square(10, 10, 10, 10)
        s.update(99, 1, 2)
        self.assertEqual("[Square] (99) 2/10 - 1", str(s))

    def test_update_args_four(self):
        """Tests Update with all arguments"""
        s = Square(10, 10, 10, 10)
        s.update(99, 1, 2, 3)
        self.assertEqual("[Square] (99) 2/3 - 1", str(s))

    def test_update_args_more_than_five(self):
        """Tests Update with more arguments"""
        s = Square(10, 10, 10, 10)
        s.update(99, 1, 2, 3, 4, 5, 6)
        self.assertEqual("[Square] (99) 2/3 - 1", str(s))

    def test_update_args_None_id(self):
        """Tests Update with id = None"""
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        """Tests Update with all arguments and id = None"""
        s = Square(10, 10, 10, 10)
        s.update(None, 2, 3, 4)
        correct = "[Square] ({}) 3/4 - 2".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        """Tests Update twice"""
        s = Square(10, 10, 10, 10)
        s.update(99, 2, 3, 4)
        s.update(2, 3, 4, 99)
        self.assertEqual("[Square] (2) 4/99 - 3", str(s))

    def test_update_args_invalid_size_type(self):
        """Tests Update with invalide size argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(99, "string")

    def test_update_args_size_zero(self):
        """Tests Update with invalide size argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(99, 0)

    def test_update_args_size_negative(self):
        """Tests Update with invalide size argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(99, -1)

    def test_update_args_invalid_x_type(self):
        """Tests Update with invalide x argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(99, 1, "string")

    def test_update_args_x_negative(self):
        """Tests Update with invalide x argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(99, 1, -2)

    def test_update_args_invalid_y(self):
        """Tests Update with invalide y argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(99, 1, 2, "string")

    def test_update_args_y_negative(self):
        """Tests Update with invalide y argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(99, 1, 2, -3)

    def test_update_args_size_before_x(self):
        """Tests Update with invalide size and x arguments"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(99, "string_1", "string_2")

    def test_update_args_size_before_y(self):
        """Tests Update with invalide size and y arguments"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(99, "string_1", 2, "string_2")

    def test_update_args_x_before_y(self):
        """Tests Update with invalide x and y arguments"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(99, 1, "string_1", "string_2")

    # Test kwargs
    def test_update_kwargs_one(self):
        """Tests Update kwargs with one argument"""
        s = Square(10, 10, 10, 10)
        s.update(id=99)
        self.assertEqual("[Square] (99) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        """Tests Update kwargs with two arguments"""
        s = Square(10, 10, 10, 10)
        s.update(id=99, size=2)
        self.assertEqual("[Square] (99) 10/10 - 2", str(s))

    def test_update_kwargs_three(self):
        """Tests Update kwargs with three arguments"""
        s = Square(10, 10, 10, 10)
        s.update(id=99, size=2, x=4)
        self.assertEqual("[Square] (99) 4/10 - 2", str(s))

    def test_update_kwargs_four(self):
        """Tests Update kwargs with all arguments"""
        s = Square(10, 10, 10, 10)
        s.update(id=99, size=2, x=4, y=5)
        self.assertEqual("[Square] (99) 4/5 - 2", str(s))

    def test_update_kwargs_None_id(self):
        """Tests Update kwargs with id = None"""
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        """Tests Update kwargs with id = None and all arguments"""
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=2, x=4, y=5)
        correct = "[Square] ({}) 4/5 - 2".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        """Tests Update kwargs twice"""
        s = Square(10, 10, 10, 10)
        s.update(id=99, x=5, size=4)
        s.update(y=6, size=3)
        self.assertEqual("[Square] (99) 5/6 - 3", str(s))

    def test_update_kwargs_invalid_size_type(self):
        """Tests Update kwargs with invalid width argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        """Tests Update kwargs with invalid width argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        """Tests Update kwargs with invalid width argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-5)

    def test_update_kwargs_inavlid_x_type(self):
        """Tests Update kwargs with invalid x argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """Tests Update kwargs with invalid x argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        """Tests Update kwargs with invalid y argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """Tests Update kwargs with invalid y argument"""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        """Tests Update kwargs with args"""
        s = Square(10, 10, 10, 10)
        s.update(99, 1, x=4, y=6)
        self.assertEqual("[Square] (99) 10/10 - 1", str(s))

    def test_update_kwargs_wrong_keys(self):
        """Tests Update kwargs with unknowen keys"""
        s = Square(10, 10, 10, 10)
        s.update(area=15, length=5)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        """Tests Update kwargs with unknowen keys"""
        s = Square(10, 10, 10, 10)
        s.update(size=3, id=99, area=15, length=5, x=12, y=12)
        self.assertEqual("[Square] (99) 12/12 - 3", str(s))


if __name__ == "__main__":
    unittest.main()
