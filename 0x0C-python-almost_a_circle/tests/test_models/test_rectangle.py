#!/usr/bin/python3
# test_rectangle.py
# Rachid BOULMANI
"""
defines unittests for rectangle.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Rectangle class.
    """

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(2, 10), Base)

    def test_no_arg(self):
        """Tests Rectangle with No arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Tests Rectangle with one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_arg(self):
        """Tests Rectangle with two arguments"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_arg(self):
        """Tests Rectangle with three arguments"""
        r1 = Rectangle(10, 2, 0)
        r2 = Rectangle(2, 10, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_arg(self):
        """Tests Rectangle with four arguments"""
        r1 = Rectangle(10, 2, 0, 0)
        r2 = Rectangle(2, 10, 1, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_all_arg(self):
        """Tests Rectangle with all arguments"""
        self.assertEqual(12, Rectangle(2, 10, 1, 1, 12).id)

    def test_more_arg(self):
        """Tests Rectangle with more arguments"""
        with self.assertRaises(TypeError):
            Rectangle(2, 10, 0, 0, 12, 1)

    def test_width_private(self):
        """Tests the private width attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_width_getter(self):
        """Tests the private width attribute's getter"""
        r = Rectangle(2, 10, 1, 1, 12)
        self.assertEqual(2, r.width)

    def test_width_setter(self):
        """Tests the private width attribute's setter"""
        r = Rectangle(2, 10, 1, 1, 12)
        r.width = 12
        self.assertEqual(12, r.width)

    def test_height_private(self):
        """Tests the private height attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 10, 1, 1, 12).__height)

    def test_height_getter(self):
        """Tests the private height attribute's getter"""
        r = Rectangle(2, 10, 1, 1, 12)
        self.assertEqual(10, r.height)

    def test_height_setter(self):
        """Tests the private height attribute's setter"""
        r = Rectangle(2, 10, 1, 1, 12)
        r.height = 12
        self.assertEqual(12, r.height)

    def test_x_private(self):
        """Tests the private x attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 10, 1, 1, 12).__x)

    def test_x_getter(self):
        """Tests the private x attribute's getter"""
        r = Rectangle(2, 10, 1, 1, 12)
        self.assertEqual(1, r.x)

    def test_x_setter(self):
        """Tests the private x attribute's setter"""
        r = Rectangle(2, 10, 1, 1, 12)
        r.x = 0
        self.assertEqual(0, r.x)

    def test_y_private(self):
        """Tests the private y attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 10, 1, 1, 12).__y)

    def test_y_getter(self):
        """Tests the private y attribute's getter"""
        r = Rectangle(2, 10, 1, 1, 12)
        self.assertEqual(1, r.y)

    def test_y_setter(self):
        """Tests the private y attribute's setter"""
        r = Rectangle(2, 10, 1, 1, 12)
        r.y = 0
        self.assertEqual(0, r.y)


class TestRectangleWidth(unittest.TestCase):
    """Unittests for testing the width attribute."""

    def test_None_width(self):
        """Tests width attribute with None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

    def test_str_width(self):
        """Tests width attribute with a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 1)

    def test_float_width(self):
        """Tests width attribute with a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.1, 1)

    def test_complex_width(self):
        """Tests width attribute with a complex"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1), 1)

    def test_dict_width(self):
        """Tests width attribute with a dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 1}, 1)

    def test_bool_width(self):
        """Tests width attribute with a boolean"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 1)

    def test_list_width(self):
        """Tests width attribute with a list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 1)

    def test_set_width(self):
        """Tests width attribute with a set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 1)

    def test_tuple_width(self):
        """Tests width attribute with a tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 1)

    def test_frozenset_width(self):
        """Tests width attribute with a frozen set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 2, 1}), 1)

    def test_range_width(self):
        """Tests width attribute with a range"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(1), 1)

    def test_bytes_width(self):
        """Tests width attribute with bytes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 1)

    def test_bytearray_width(self):
        """Tests width attribute with a byte array"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'Python'), 1)

    def test_memoryview_width(self):
        """Tests width attribute with a memory view"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'Python'), 1)

    def test_inf_width(self):
        """Tests width attribute with Inf"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 1)

    def test_nan_width(self):
        """Tests width attribute with NaN"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 1)

    def test_negative_width(self):
        """Tests width attribute with a negative value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)

    def test_zero_width(self):
        """Tests width attribute with 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)


class TestRectangleHeight(unittest.TestCase):
    """Unittests for testing the height attribute."""

    def test_None_height(self):
        """Tests height attribute with None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        """Tests height attribute with a string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        """Tests height attribute with a float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1.1)

    def test_complex_height(self):
        """Tests height attribute with a complex"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(1))

    def test_dict_height(self):
        """Tests height attribute with a dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 1})

    def test_list_height(self):
        """Tests height attribute with a list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        """Tests height attribute with a set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        """Tests height attribute with a tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        """Tests height attribute with a frozen set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 2, 1}))

    def test_range_height(self):
        """Tests height attribute with a range"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        """Tests height attribute with bytes"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_bytearray_height(self):
        """Tests height attribute with a byte array"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'Python'))

    def test_memoryview_height(self):
        """Tests height attribute with a memory view"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'Python'))

    def test_inf_height(self):
        """Tests height attribute with Inf"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan_height(self):
        """Tests height attribute with NaN"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative_height(self):
        """Tests height attribute with a negative value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        """Tests height attribute with 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangleX(unittest.TestCase):
    """Unittests for testing the x attribute."""

    def test_None_x(self):
        """Tests x attribute with None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 0)

    def test_str_x(self):
        """Tests x attribute with a string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "invalid", 0)

    def test_float_x(self):
        """Tests x attribute with a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, 0.0, 0)

    def test_complex_x(self):
        """Tests x attribute with a complex"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, complex(0), 0)

    def test_dict_x(self):
        """Tests x attribute with a dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {"a": 0, "b": 0}, 0)

    def test_bool_x(self):
        """Tests x attribute with a boolean"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, True, 0)

    def test_list_x(self):
        """Tests x attribute with a list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, [1, 2, 3], 0)

    def test_set_x(self):
        """Tests x attribute with a set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {1, 2, 3}, 0)

    def test_tuple_x(self):
        """Tests x attribute with a tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, (1, 2, 3), 0)

    def test_frozenset_x(self):
        """Tests x attribute with a frozen set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, frozenset({1, 2, 3, 1}), 0)

    def test_range_x(self):
        """Tests x attribute with a range"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, range(1), 0)

    def test_bytes_x(self):
        """Tests x attribute with bytes"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, b'Python', 0)

    def test_bytearray_x(self):
        """Tests x attribute with a byte array"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, bytearray(b'Python'), 0)

    def test_memoryview_x(self):
        """Tests x attribute with a memory view"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, memoryview(b'Python'), 0)

    def test_inf_x(self):
        """Tests x attribute with a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, float('inf'), 0)

    def test_nan_x(self):
        """Tests x attribute with a Nan"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, float('nan'), 0)

    def test_negative_x(self):
        """Tests x attribute with a negative value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 0)


class TestRectangleY(unittest.TestCase):
    """Unittests for testing the y attribute."""

    def test_None_y(self):
        """Tests y attribute with None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, None)

    def test_str_y(self):
        """Tests y attribute with a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, "invalid")

    def test_float_y(self):
        """Tests y attribute with a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, 0.0)

    def test_complex_y(self):
        """Tests y attribute with a complex"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, complex(0))

    def test_dict_y(self):
        """Tests y attribute with a dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, {"a": 0, "b": 0})

    def test_bool_y(self):
        """Tests y attribute with a boolean"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, True)

    def test_list_y(self):
        """Tests y attribute with a list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, [1, 2, 3])

    def test_set_y(self):
        """Tests y attribute with a set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, {1, 2, 3})

    def test_tuple_y(self):
        """Tests y attribute with a tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, (1, 2, 3))

    def test_frozenset_y(self):
        """Tests y attribute with a frozen set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        """Tests y attribute with a range"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, range(1))

    def test_bytes_y(self):
        """Tests y attribute with bytes"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, b'Python')

    def test_bytearray_y(self):
        """Tests y attribute with a byte array"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, bytearray(b'Python'))

    def test_memoryview_y(self):
        """Tests y attribute with a memory view"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, memoryview(b'Python'))

    def test_inf_y(self):
        """Tests y attribute with a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, float('inf'))

    def test_nan_y(self):
        """Tests y attribute with a Nan"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 0, float('nan'))

    def test_negative_y(self):
        """Tests y attribute with a negative value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 0, -1)


class TestRectangleInitializationOrder(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        """Tests width before height"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        """Tests width before x"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 1, "invalid x")

    def test_width_before_y(self):
        """Tests width before y"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 1, 0, "invalid y")

    def test_height_before_x(self):
        """Tests height before x"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        """Tests height before y"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 0, "invalid y")

    def test_x_before_y(self):
        """Tests x before y"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "invalid x", "invalid y")


if __name__ == "__main__":
    unittest.main()
