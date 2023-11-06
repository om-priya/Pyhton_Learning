"""
Filename must start with test_ bcoz that's what default config of unitesting look at
same for the function in testclass it should start with test_
"""
# To run this file python -m unittest <filename>
from unittest import TestCase
from app import multiply, divide


class TestFunction(TestCase):
    def test_divide_function(self):  # Function should start with test_
        print("test1")
        dividend = 10  # variable for testing
        divisor = 2
        expected_result = 5.0  # expected result
        # use assertAlmostEqual while comparing floating numbers
        self.assertAlmostEqual(
            divide(dividend, divisor), expected_result, delta=0.000001
        )

    def test_divide_negative(self):
        print("test2")
        dividend = -10  # variable for testing
        divisor = 2
        expected_result = -5.0  # expected result
        self.assertAlmostEqual(
            divide(dividend, divisor), expected_result, delta=0.000001
        )

    def test_divide_dividend_zero(self):
        print("test3")
        dividend = 0  # variable for testing
        divisor = 2
        expected_result = 0  # expected result
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_divisor_zero(self):
        print("test4")
        with self.assertRaises(ValueError):
            # divide(25, 5) result in failure because exception not raised
            divide(25, 0)

    def test_multiply_only_zero(self):
        print("test5")
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply(self):
        print("test6")
        values = (3, 5, 2)
        expected = 30

        self.assertEqual(multiply(*values), expected)

    def test_multiply_zero(self):
        print("test7")
        values = (3, 5, 0)
        expected = 0

        self.assertEqual(multiply(*values), expected)

    def test_multiply_noargs(self):
        print("test8")
        self.assertRaises(ValueError, multiply)
