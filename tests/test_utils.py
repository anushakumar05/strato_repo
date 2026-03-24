import unittest
from src.utils import calculate_cube_volume

class TestCalculateCubeVolume(unittest.TestCase):

    def test_positive_integer_side(self):
        """Test with a positive integer-like float side length."""
        self.assertAlmostEqual(calculate_cube_volume(5.0), 125.0)

    def test_positive_decimal_side(self):
        """Test with a positive decimal float side length."""
        self.assertAlmostEqual(calculate_cube_volume(2.5), 15.625)

    def test_zero_side(self):
        """Test with a zero side length."""
        self.assertAlmostEqual(calculate_cube_volume(0.0), 0.0)

    def test_negative_side_raises_value_error(self):
        """Test that a negative side length raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "Side length cannot be negative."):
            calculate_cube_volume(-4.0)

if __name__ == '__main__':
    unittest.main()