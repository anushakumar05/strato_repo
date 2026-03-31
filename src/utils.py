import math

def calculate_cube_volume(side: float) -> float:
    """
    Calculates the volume of a cube given its side length.

    Args:
        side (float): The length of one side of the cube.

    Returns:
        float: The volume of the cube.

    Raises:
        ValueError: If the side length is negative.
    """
    if side < 0:
        raise ValueError("Side length cannot be negative.")
    return side ** 3

def sort_array(arr: list) -> list:
    """
    Sorts a list of comparable elements in ascending order.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.

    Raises:
        TypeError: If the input is not a list, or if elements in the list are not comparable.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    
    # Python's built-in sorted() function handles sorting of various comparable types
    # and raises TypeError for non-comparable types within the list.
    return sorted(arr)

if __name__ == '__main__':
    # Example usage for calculate_cube_volume
    print(f"Volume of a cube with side 5: {calculate_cube_volume(5.0)}")
    print(f"Volume of a cube with side 2.5: {calculate_cube_volume(2.5)}")
    print(f"Volume of a cube with side 0: {calculate_cube_volume(0.0)}")

    # Example of error handling for calculate_cube_volume
    try:
        calculate_cube_volume(-4.0)
    except ValueError as e:
        print(f"Error: {e}")

    print("\n--- sort_array examples ---")
    # Example usage for sort_array
    list1 = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original list: {list1}")
    print(f"Sorted list: {sort_array(list1)}")

    list2 = ["banana", "apple", "cherry"]
    print(f"Original list: {list2}")
    print(f"Sorted list: {sort_array(list2)}")

    list3 = []
    print(f"Original list: {list3}")
    print(f"Sorted list: {sort_array(list3)}")

    list4 = [7.5, 2.1, 10.0, 0.5]
    print(f"Original list: {list4}")
    print(f"Sorted list: {sort_array(list4)}")

    # Example of error handling for sort_array
    try:
        sort_array("not a list")
    except TypeError as e:
        print(f"Error sorting non-list input: {e}")

    try:
        # This will raise TypeError because int and str are not comparable
        sort_array([1, 5, "hello", 3])
    except TypeError as e:
        print(f"Error sorting list with non-comparable elements: {e}")