#!/usr/bin/python3
# test_base.py
# Rachid BOULMANI
"""
defines unittests for base.py
"""

import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Base class.
    """

    def test_no_arg(self):
        """Tests two bases with No arguments"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """Tests three bases with No arguments"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1, b3.id - 2)

    def test_None_id(self):
        """Tests two bases with 'None' argument"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """Tests instantiation with id argument id = 12"""
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        """Tests instantiation after an id argument id = 12"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        """Tests the id attribute"""
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """Tests the nb_instances attribute"""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        """Tests instantiation with a string argument"""
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        """Tests instantiation with a float argument"""
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        """Tests instantiation with a complex argument"""
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        """Tests instantiation with a dictionary argument"""
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        """Tests instantiation with a boolean argument"""
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """Tests instantiation with a list argument"""
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        """Tests instantiation with a tuple as argument"""
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        """Tests instantiation with a set as argument"""
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        """Tests instantiation with a frozen set as argument"""
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        """Tests instantiation with a range as argument"""
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        """Tests instantiation with bytes as argument"""
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        """Tests instantiation with bytes array as argument"""
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        """Tests instantiation with memory iew as argument"""
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        """Tests instantiation with infinity float as argument"""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """Tests instantiation with NaN as argument"""
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        """Tests instantiation with more than one argument"""
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
