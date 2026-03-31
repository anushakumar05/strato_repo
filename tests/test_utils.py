import unittest
from src.utils import calculate_cube_volume, sort_array

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

class TestSortArray(unittest.TestCase):

    def test_sort_integers(self):
        """Test sorting an array of integers."""
        self.assertEqual(sort_array([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_sort_floats(self):
        """Test sorting an array of floats."""
        self.assertAlmostEqual(sort_array([3.1, 1.4, 4.1, 1.5, 9.2, 2.6]), [1.4, 1.5, 2.6, 3.1, 4.1, 9.2])

    def test_sort_mixed_numbers(self):
        """Test sorting an array of mixed integers and floats."""
        self.assertAlmostEqual(sort_array([3, 1.5, 4.0, 1, 5.5, 9, 2.1, 6]), [1, 1.5, 2.1, 3, 4.0, 5.5, 6, 9])

    def test_sort_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        self.assertEqual(sort_array([-3, -1, -4, 0, 1, -5]), [-5, -4, -3, -1, 0, 1])

    def test_already_sorted_array(self):
        """Test sorting an array that is already sorted."""
        self.assertEqual(sort_array([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """Test sorting an array that is reverse sorted."""
        self.assertEqual(sort_array([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        """Test sorting an array containing duplicate values."""
        self.assertEqual(sort_array([5, 1, 3, 5, 2, 1]), [1, 1, 2, 3, 5, 5])

    def test_empty_array(self):
        """Test sorting an empty array."""
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        """Test sorting an array with a single element."""
        self.assertEqual(sort_array([42]), [42])

    def test_non_list_input_raises_type_error(self):
        """Test that non-list input raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "Input must be a list."):
            sort_array("not a list")
        with self.assertRaisesRegex(TypeError, "Input must be a list."):
            sort_array(123)

    def test_list_with_non_numeric_elements_raises_type_error(self):
        """Test that a list containing non-numeric elements raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "All elements in the list must be numbers."):
            sort_array([1, 2, 'a', 4])
        with self.assertRaisesRegex(TypeError, "All elements in the list must be numbers."):
            sort_array([1, None, 3])
        with self.assertRaisesRegex(TypeError, "All elements in the list must be numbers."):
            sort_array([1, [2, 3]])

if __name__ == '__main__':
    unittest.main()