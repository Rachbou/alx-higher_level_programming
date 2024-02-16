#!/usr/bin/python3

"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer([..])."""
    
    def test_empty_list(self):
        """Tests an empty list."""
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        test_list = [10]
        self.assertEqual(max_integer(test_list), 10)

    def test_ascending_sortered_list(self):
        """Tests an ascending sortered list of integers."""
        test_list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_integer(test_list), 6)

    def test_descending_sortered_list(self):
        """Tests a descending sortered list of integers."""
        test_list = [6, 5, 4, 3, 2, 1]
        self.assertEqual(max_integer(test_list), 6)

    def test_unsortered_list(self):
        """Test an unordered list of integers."""
        test_list = [4, 0, 6, 10, 2, 8]
        self.assertEqual(max_integer(test_list), 10)

    def test_floats(self):
        """Test a list of floats."""
        test_list = [2.1, 10.9, 8.7, 4.3, 6.5]
        self.assertEqual(max_integer(test_list), 10.9)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        test_list = [2, 1.0, 9.5, 8.7, 4, 3, 6.5]
        self.assertEqual(max_integer(test_list), 9.5)

    def test_upper_string(self):
        """Test a string."""
        test_string = "boulmani"
        self.assertEqual(max_integer(test_string), 'u')
    
    def test_lower_string(self):
        """Test a string."""
        test_string = "BOULMANI"
        self.assertEqual(max_integer(test_string), 'U')

    def test_mixed_string(self):
        """Test a string."""
        test_string = "BoUlMaNi"
        self.assertEqual(max_integer(test_string), 'o')

    def test_list_of_non_numbers(self):
        """Test a list of strings."""
        test_list = ["Rachid", "Boulmani", "alx", "Python"]
        self.assertEqual(max_integer(test_list), "alx")

if __name__ == '__main__':
    unittest.main()
