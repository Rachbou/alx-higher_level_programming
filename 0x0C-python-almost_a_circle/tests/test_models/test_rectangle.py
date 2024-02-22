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


if __name__ == "__main__":
    unittest.main()
