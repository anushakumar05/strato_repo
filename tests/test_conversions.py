import unittest
import sys
import os

# Adjust the path to import from the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

try:
    from conversions import decimal_to_binary, celsius_to_fahrenheit
except ImportError as e:
    print(f"Error importing functions from src/conversions.py: {e}")
    print("Please ensure src/conversions.py exists and contains the required functions.")
    sys.exit(1)


class TestConversions(unittest.TestCase):
    """
    Unit tests for the conversion functions in src/conversions.py.
    """

    def test_decimal_to_binary_positive_integers(self):
        """
        Test decimal_to_binary with positive integer inputs.
        """
        self.assertEqual(decimal_to_binary(0), "0")
        self.assertEqual(decimal_to_binary(1), "1")
        self.assertEqual(decimal_to_binary(2), "10")
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(255), "11111111")
        self.assertEqual(decimal_to_binary(1024), "10000000000")

    def test_decimal_to_binary_invalid_types(self):
        """
        Test decimal_to_binary with non-integer inputs.
        """
        with self.assertRaises(TypeError):
            decimal_to_binary(3.14)
        with self.assertRaises(TypeError):
            decimal_to_binary("10")
        with self.assertRaises(TypeError):
            decimal_to_binary(None)
        with self.assertRaises(TypeError):
            decimal_to_binary([10])

    def test_decimal_to_binary_negative_input(self):
        """
        Test decimal_to_binary with negative integer input, which should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            decimal_to_binary(-5)

    def test_celsius_to_fahrenheit_known_values(self):
        """
        Test celsius_to_fahrenheit with standard and edge case values.
        """
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0) # -40C is -40F
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(37.78), 100.004) # Example with float input

    def test_celsius_to_fahrenheit_zero(self):
        """
        Test celsius_to_fahrenheit with zero input.
        """
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)

    def test_celsius_to_fahrenheit_negative_values(self):
        """
        Test celsius_to_fahrenheit with negative Celsius temperatures.
        """
        self.assertAlmostEqual(celsius_to_fahrenheit(-10), 14.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(-20), -4.0)

    def test_celsius_to_fahrenheit_invalid_types(self):
        """
        Test celsius_to_fahrenheit with non-numeric inputs.
        """
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("abc")
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit(None)
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit([10])


if __name__ == '__main__':
    unittest.main()