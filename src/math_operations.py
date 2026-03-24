import math

def calculate_sphere_volume(radius: float) -> float:
    """
    Calculates the volume of a sphere given its radius.

    The formula used is V = (4/3) * pi * r^3.

    Args:
        radius (float): The radius of the sphere. Must be a non-negative number.

    Returns:
        float: The calculated volume of the sphere.

    Raises:
        TypeError: If the radius is not a number (int or float).
        ValueError: If the radius is negative.

    Example:
        >>> calculate_sphere_volume(1.0)
        4.1887902047863905
        >>> calculate_sphere_volume(0)
        0.0
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number (int or float).")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    volume = (4/3) * math.pi * (radius ** 3)
    return volume