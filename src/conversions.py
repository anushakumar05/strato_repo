import math

def decimal_to_binary(decimal_num: int) -> str:
    """
    Converts a non-negative decimal integer to its binary string representation.

    Args:
        decimal_num (int): The non-negative integer to convert.

    Returns:
        str: A string representing the binary equivalent of the input number.

    Raises:
        TypeError: If the input `decimal_num` is not an integer.
        ValueError: If the input `decimal_num` is negative.

    Examples:
        >>> decimal_to_binary(0)
        '0'
        >>> decimal_to_binary(1)
        '1'
        >>> decimal_to_binary(10)
        '1010'
        >>> decimal_to_binary(255)
        '11111111'
    """
    if not isinstance(decimal_num, int):
        raise TypeError("Input 'decimal_num' must be an integer.")
    
    if decimal_num < 0:
        raise ValueError("Input 'decimal_num' must be a non-negative integer.")

    if decimal_num == 0:
        return "0"

    # Python's built-in bin() function returns a string prefixed with '0b'.
    # We slice the string to remove this prefix.
    return bin(decimal_num)[2:]

if __name__ == "__main__":
    # Example usage and basic testing
    print(f"Decimal 0 to Binary: {decimal_to_binary(0)}")
    print(f"Decimal 1 to Binary: {decimal_to_binary(1)}")
    print(f"Decimal 10 to Binary: {decimal_to_binary(10)}")
    print(f"Decimal 255 to Binary: {decimal_to_binary(255)}")
    print(f"Decimal 1024 to Binary: {decimal_to_binary(1024)}")

    # Test error handling
    try:
        decimal_to_binary(-5)
    except ValueError as e:
        print(f"Error for -5: {e}")

    try:
        decimal_to_binary(3.14)
    except TypeError as e:
        print(f"Error for 3.14: {e}")

    try:
        decimal_to_binary("hello")
    except TypeError as e:
        print(f"Error for 'hello': {e}")