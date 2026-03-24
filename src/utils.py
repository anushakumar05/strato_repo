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

if __name__ == '__main__':
    # Example usage
    print(f"Volume of a cube with side 5: {calculate_cube_volume(5.0)}")
    print(f"Volume of a cube with side 2.5: {calculate_cube_volume(2.5)}")
    print(f"Volume of a cube with side 0: {calculate_cube_volume(0.0)}")

    # Example of error handling
    try:
        calculate_cube_volume(-4.0)
    except ValueError as e:
        print(f"Error: {e}")