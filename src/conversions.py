import math

def decimal_to_binary(decimal_num: int) -> str:
    """
    Converts a non-negative integer decimal number to its binary string representation.

    Args:
        decimal_num (int): The non-negative integer decimal number to convert.

    Returns:
        str: The binary representation of the decimal number.

    Raises:
        TypeError: If `decimal_num` is not an integer.
        ValueError: If `decimal_num` is a negative integer.

    Examples:
        >>> decimal_to_binary(0)
        '0'
        >>> decimal_to_binary(1)
        '1'
        >>> decimal_to_binary(2)
        '10'
        >>> decimal_to_binary(10)
        '1010'
        >>> decimal_to_binary(255)
        '11111111'
    """
    if not isinstance(decimal_num, int):
        raise TypeError("Input must be an integer.")
    
    if decimal_num < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if decimal_num == 0:
        return "0"
    
    binary_string = ""
    temp_num = decimal_num
    
    while temp_num > 0:
        remainder = temp_num % 2
        binary_string = str(remainder) + binary_string
        temp_num //= 2
        
    return binary_string

# You can add other conversion-related functions here in the future,
# such as binary_to_decimal, hex_to_decimal, etc.