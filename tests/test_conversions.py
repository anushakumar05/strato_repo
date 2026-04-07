import pytest
from src.conversions import decimal_to_binary

class TestDecimalToBinary:
    """
    Test suite for the `decimal_to_binary` function, ensuring it correctly converts
    non-negative integers to their binary string representation and handles invalid inputs.
    """

    @pytest.mark.parametrize("decimal_input, expected_binary", [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (4, "100"),
        (5, "101"),
        (10, "1010"),
        (15, "1111"),
        (16, "10000"),
        (32, "100000"),
        (255, "11111111"),
        (1024, "10000000000"),
        (65535, "1111111111111111"), # Max 16-bit unsigned
    ])
    def test_valid_positive_integers(self, decimal_input, expected_binary):
        """
        Test that `decimal_to_binary` correctly converts various non-negative integers
        to their binary string representation.
        """
        assert decimal_to_binary(decimal_input) == expected_binary

    def test_zero_input(self):
        """
        Test that `decimal_to_binary` correctly handles an input of zero.
        """
        assert decimal_to_binary(0) == "0"

    def test_negative_integer_raises_value_error(self):
        """
        Test that `decimal_to_binary` raises a ValueError for negative integer inputs,
        as binary conversion is typically defined for non-negative numbers.
        """
        with pytest.raises(ValueError, match="Input must be a non-negative integer"):
            decimal_to_binary(-1)
        with pytest.raises(ValueError, match="Input must be a non-negative integer"):
            decimal_to_binary(-100)

    @pytest.mark.parametrize("invalid_input", [
        1.5,       # Float with fractional part
        "10",      # String
        None,      # None type
        [1, 0],    # List
        {"key": 10}, # Dictionary
        True,      # Boolean (which is subclass of int, but for strict type checking assume disallowed)
                   # If the function strictly checks `isinstance(n, int)` and not `isinstance(n, (int, bool))`,
                   # then True/False would raise TypeError. Let's assume standard integer check.
    ])
    def test_invalid_types_raise_type_error(self, invalid_input):
        """
        Test that `decimal_to_binary` raises a TypeError for inputs that are not integers.
        """
        with pytest.raises(TypeError, match="Input must be an integer"):
            decimal_to_binary(invalid_input)

    def test_float_integer_raises_type_error(self):
        """
        Test that `decimal_to_binary` raises a TypeError even for float inputs that
        numerically represent an integer (e.g., 5.0), adhering to strict integer typing.
        """
        with pytest.raises(TypeError, match="Input must be an integer"):
            decimal_to_binary(5.0)
        with pytest.raises(TypeError, match="Input must be an integer"):
            decimal_to_binary(0.0)