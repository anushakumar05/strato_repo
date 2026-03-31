import collections

def reverse_array(arr: collections.abc.Sequence) -> list:
    """
    Reverses the order of elements in a sequence and returns a new list.

    This function takes any sequence (like a list, tuple, or string)
    and returns a new list with its elements in reverse order.
    The original sequence remains unchanged.

    Args:
        arr (collections.abc.Sequence): The input sequence to be reversed.

    Returns:
        list: A new list containing the elements of the input sequence
              in reverse order.

    Raises:
        TypeError: If the input `arr` is not a sequence.

    Examples:
        >>> reverse_array([1, 2, 3])
        [3, 2, 1]
        >>> reverse_array(['a', 'b', 'c'])
        ['c', 'b', 'a']
        >>> reverse_array("hello")
        ['o', 'l', 'l', 'e', 'h']
        >>> reverse_array([])
        []
        >>> reverse_array((10, 20))
        [20, 10]
    """
    if not isinstance(arr, collections.abc.Sequence):
        raise TypeError("Input must be a sequence (e.g., list, tuple, string).")
    
    # Using slicing to create a reversed copy of the sequence.
    # We convert it to a list to ensure the return type is consistently a list.
    return list(arr[::-1])