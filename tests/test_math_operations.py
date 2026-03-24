import unittest
import math
from src.math_operations import calculate_sphere_volume

class TestCalculateSphereVolume(unittest.TestCase):

    def test_positive_float_radius(self):
        # Test with a standard positive float radius
        radius = 1.0
        expected_volume = (4/3) * math.pi * (radius ** 3)
        self.assertAlmostEqual(calculate_sphere_volume(radius), expected_volume)

        radius = 2.5
        expected_volume = (4/3) * math.pi * (radius ** 3)
        self.assertAlmostEqual(calculate_sphere_volume(radius), expected_volume)

    def test_positive_integer_radius(self):
        # Test with a positive integer radius
        radius = 2
        expected_volume = (4/3) * math.pi * (radius ** 3)
        self.assertAlmostEqual(calculate_sphere_volume(radius), expected_volume)

        radius = 0
        expected_volume = 0.0
        self.assertAlmostEqual(calculate_sphere_volume(radius), expected_volume)

    def test_zero_radius(self):
        # Test with zero radius, volume should be 0.0
        self.assertAlmostEqual(calculate_sphere_volume(0), 0.0)
        self.assertAlmostEqual(calculate_sphere_volume(0.0), 0.0)

    def test_type_error_for_non_numeric_radius(self):
        # Test that TypeError is raised for non-numeric input
        with self.assertRaisesRegex(TypeError, "Radius must be a number \(int or float\)."):
            calculate_sphere_volume("abc")
        with self.assertRaisesRegex(TypeError, "Radius must be a number \(int or float\)."):
            calculate_sphere_volume(None)
        with self.assertRaisesRegex(TypeError, "Radius must be a number \(int or float\)."):
            calculate_sphere_volume([1])

    def test_value_error_for_negative_radius(self):
        # Test that ValueError is raised for negative radius
        with self.assertRaisesRegex(ValueError, "Radius cannot be negative."):
            calculate_sphere_volume(-1.0)
        with self.assertRaisesRegex(ValueError, "Radius cannot be negative."):
            calculate_sphere_volume(-5)

if __name__ == '__main__':
    unittest.main()