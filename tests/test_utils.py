import unittest
from src.utils import reverse_array

class TestReverseArray(unittest.TestCase):
    """
    Unit tests for the reverse_array function found in src/utils.py.
    This suite covers various scenarios including empty lists, single-element lists,
    lists of different lengths, mixed data types, and ensures proper type handling.
    """

    def test_empty_list(self):
        """
        Test that reverse_array correctly handles an empty list,
        returning an empty list.
        """
        self.assertEqual(reverse_array([]), [])

    def test_single_element_list(self):
        """
        Test that reverse_array correctly handles a list with a single element,
        returning the same list.
        """
        self.assertEqual(reverse_array([1]), [1])
        self.assertEqual(reverse_array(['a']), ['a'])

    def test_even_length_list(self):
        """
        Test reverse_array with a list containing an even number of elements.
        """
        self.assertEqual(reverse_array([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(reverse_array(['a', 'b', 'c', 'd']), ['d', 'c', 'b', 'a'])

    def test_odd_length_list(self):
        """
        Test reverse_array with a list containing an odd number of elements.
        """
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_array(['x', 'y', 'z']), ['z', 'y', 'x'])

    def test_mixed_type_list(self):
        """
        Test reverse_array with a list containing elements of mixed data types.
        """
        input_list = [1, "hello", 3.14, True, None, ['nested']]
        expected_list = [['nested'], None, True, 3.14, "hello", 1]
        self.assertEqual(reverse_array(input_list), expected_list)

    def test_original_list_unchanged(self):
        """
        Test that the reverse_array function returns a new list and does not
        modify the original list in-place.
        """
        original_list = [10, 20, 30, 40]
        reversed_list = reverse_array(original_list)

        # Check that the original list remains unchanged
        self.assertEqual(original_list, [10, 20, 30, 40])
        # Check that the returned list is indeed reversed
        self.assertEqual(reversed_list, [40, 30, 20, 10])
        # Check that the returned list is a new object, not the original list
        self.assertIsNot(original_list, reversed_list)

    def test_non_list_input_raises_type_error(self):
        """
        Test that reverse_array raises a TypeError when input is not a list.
        """
        with self.assertRaises(TypeError):
            reverse_array("a string")
        with self.assertRaises(TypeError):
            reverse_array(123)
        with self.assertRaises(TypeError):
            reverse_array(None)
        with self.assertRaises(TypeError):
            reverse_array({'key': 'value'})
        with self.assertRaises(TypeError):
            reverse_array((1, 2, 3)) # Tuple is also not a list


if __name__ == '__main__':
    unittest.main()