import unittest
# Assuming the file is located at src/array_utils.py
from src.array_utils import find_element_in_array

class TestFindElementInArray(unittest.TestCase):

    # --- Happy Path: Element Found ---

    def test_element_found_in_list_of_integers(self):
        self.assertEqual(find_element_in_array([1, 2, 3, 4, 5], 3), 2)

    def test_element_found_in_list_of_strings(self):
        self.assertEqual(find_element_in_array(['apple', 'banana', 'cherry'], 'banana'), 1)

    def test_element_found_in_mixed_type_list(self):
        self.assertEqual(find_element_in_array([1, "hello", 3.14, True], "hello"), 1)

    def test_element_found_at_start_of_list(self):
        self.assertEqual(find_element_in_array([10, 20, 30], 10), 0)

    def test_element_found_at_end_of_list(self):
        self.assertEqual(find_element_in_array([10, 20, 30], 30), 2)

    def test_finds_first_occurrence_of_duplicate_element(self):
        self.assertEqual(find_element_in_array([1, 2, 3, 2, 4], 2), 1)

    def test_finds_zero(self):
        self.assertEqual(find_element_in_array([-1, 0, 1], 0), 1)

    def test_finds_none_element(self):
        self.assertEqual(find_element_in_array([1, None, 3], None), 1)

    # --- Happy Path: Element Not Found ---

    def test_element_not_found_in_list_of_integers(self):
        self.assertEqual(find_element_in_array([1, 2, 3], 4), -1)

    def test_element_not_found_in_list_of_strings(self):
        self.assertEqual(find_element_in_array(['a', 'b', 'c'], 'd'), -1)

    def test_element_not_found_in_empty_list(self):
        self.assertEqual(find_element_in_array([], 1), -1)

    def test_element_not_found_different_type(self):
        # Element 1 (int) is not found when searching for 1.0 (float)
        self.assertEqual(find_element_in_array([1, 2, 3], 1.0), -1)
        # Element True is not found when searching for False (False != 1)
        self.assertEqual(find_element_in_array([1, "hello", 3.14, True], False), -1)

    # --- Error Handling ---

    def test_raises_type_error_if_arr_is_string(self):
        with self.assertRaises(TypeError) as cm:
            find_element_in_array("this is a string", 'a')
        self.assertIn("Input 'arr' must be a list or a sequence type (excluding string).", str(cm.exception))

    def test_raises_type_error_if_arr_is_int(self):
        with self.assertRaises(TypeError) as cm:
            find_element_in_array(123, 1)
        self.assertIn("Input 'arr' must be a list or a sequence type (excluding string).", str(cm.exception))

    def test_raises_type_error_if_arr_is_float(self):
        with self.assertRaises(TypeError) as cm:
            find_element_in_array(3.14, 1)
        self.assertIn("Input 'arr' must be a list or a sequence type (excluding string).", str(cm.exception))

    def test_raises_type_error_if_arr_is_none(self):
        with self.assertRaises(TypeError) as cm:
            find_element_in_array(None, 5)
        self.assertIn("Input 'arr' must be a list or a sequence type (excluding string).", str(cm.exception))
    
    def test_raises_type_error_if_arr_is_dict(self):
        with self.assertRaises(TypeError) as cm:
            find_element_in_array({'a': 1, 'b': 2}, 'a')
        self.assertIn("Input 'arr' must be a list or a sequence type (excluding string).", str(cm.exception))

    def test_raises_type_error_if_arr_is_set(self):
        with self.assertRaises(TypeError) as cm:
            find_element_in_array({1, 2, 3}, 1)
        self.assertIn("Input 'arr' must be a list or a sequence type (excluding string).", str(cm.exception))

    # --- Other Sequence Types (should NOT raise TypeError) ---

    def test_find_element_in_tuple(self):
        # Tuples are collections.abc.Sequence and not strings, so they should work
        self.assertEqual(find_element_in_array((1, 2, 3), 2), 1)
        self.assertEqual(find_element_in_array((1, 2, 3), 4), -1)

    def test_find_element_in_bytes(self):
        # Bytes are collections.abc.Sequence and not strings, so they should work
        self.assertEqual(find_element_in_array(b'abc', ord('b')), 1)
        self.assertEqual(find_element_in_array(b'abc', ord('d')), -1)

    def test_find_element_in_range(self):
        # Range objects are collections.abc.Sequence and not strings, so they should work
        self.assertEqual(find_element_in_array(range(5), 3), 3)
        self.assertEqual(find_element_in_array(range(5), 5), -1)

if __name__ == '__main__':
    unittest.main()