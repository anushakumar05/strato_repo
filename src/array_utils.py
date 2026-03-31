import collections.abc

def find_element_in_array(arr: list, element: object) -> int:
    """
    Searches for a given 'element' within the 'arr' list.

    Returns the index of the first occurrence if found, otherwise returns -1.

    Args:
        arr (list): The list to search within.
        element (object): The element to search for.

    Returns:
        int: The index of the first occurrence of the element if found,
             otherwise -1.

    Raises:
        TypeError: If 'arr' is not a list.

    Example:
        >>> find_element_in_array([1, 2, 3, 4, 5], 3)
        2
        >>> find_element_in_array(['a', 'b', 'c'], 'd')
        -1
        >>> find_element_in_array([], 1)
        -1
    """
    if not isinstance(arr, collections.abc.Sequence) or isinstance(arr, str):
        raise TypeError("Input 'arr' must be a list or a sequence type (excluding string).")
    
    # Python's list.index() method raises ValueError if the element is not found.
    # We need to return -1 in that case, so a try-except block is suitable.
    try:
        return arr.index(element)
    except ValueError:
        return -1

if __name__ == '__main__':
    # Example Usage:
    my_list = [10, 20, 30, 40, 50]
    
    # Test case 1: Element found
    element_to_find = 30
    index = find_element_in_array(my_list, element_to_find)
    print(f"Element {element_to_find} found at index: {index}") # Expected: 2

    # Test case 2: Element not found
    element_to_find = 60
    index = find_element_in_array(my_list, element_to_find)
    print(f"Element {element_to_find} found at index: {index}") # Expected: -1

    # Test case 3: Empty list
    empty_list = []
    element_to_find = 5
    index = find_element_in_array(empty_list, element_to_find)
    print(f"Element {element_to_find} found in empty list at index: {index}") # Expected: -1

    # Test case 4: List with duplicates, finds first occurrence
    duplicate_list = [1, 2, 3, 2, 4]
    element_to_find = 2
    index = find_element_in_array(duplicate_list, element_to_find)
    print(f"Element {element_to_find} found in duplicate list at index: {index}") # Expected: 1

    # Test case 5: Different data types
    mixed_list = [1, "hello", 3.14, True]
    element_to_find = "hello"
    index = find_element_in_array(mixed_list, element_to_find)
    print(f"Element '{element_to_find}' found in mixed list at index: {index}") # Expected: 1

    element_to_find = False
    index = find_element_in_array(mixed_list, element_to_find) # True is 1, False is 0 in some contexts
    print(f"Element '{element_to_find}' found in mixed list at index: {index}") # Expected: -1 (False != 1)

    # Test case 6: Error handling (non-list input)
    try:
        find_element_in_array("this is a string", 'a')
    except TypeError as e:
        print(f"Caught expected error: {e}") # Expected: TypeError

    try:
        find_element_in_array(None, 5)
    except TypeError as e:
        print(f"Caught expected error: {e}") # Expected: TypeError