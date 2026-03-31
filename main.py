import sys
from typing import List, Any

# Assume these functions exist in src/utils.py based on the README updates.
# An ImportError is caught to provide a user-friendly message if they are missing.
try:
    from src.utils import add
    from src.utils import celsius_to_fahrenheit
    from src.utils import fahrenheit_to_celsius
    from src.utils import reverse_array
except ImportError:
    print(
        "Error: Could not import one or more utility functions from 'src.utils'. "
        "Please ensure 'src/utils.py' exists and contains 'add', 'celsius_to_fahrenheit', "
        "'fahrenheit_to_celsius', and 'reverse_array' functions.",
        file=sys.stderr
    )
    sys.exit(1)


def display_help():
    """
    Displays the help message for the command-line interface, outlining available
    commands and their usage.
    """
    help_message = """
Usage: python main.py <command> [arguments]

Available commands:
  add <num1> <num2>
    Adds two numbers together.
    Arguments:
      <num1>: The first number (float).
      <num2>: The second number (float).
    Example: python main.py add 5 3  # Returns 8.0

  convert <value> [unit]
    Converts temperature between Celsius and Fahrenheit.
    Arguments:
      <value>: The temperature value to convert (float).
      [unit]: Optional. The unit of the input value. Can be 'C' (Celsius) or 'F' (Fahrenheit). Defaults to 'C'.
    Example: python main.py convert 25 C  # Converts 25 Celsius to Fahrenheit
    Example: python main.py convert 77 F  # Converts 77 Fahrenheit to Celsius

  reverse-array <element1> <element2> ...
    Reverses the order of provided array elements.
    Arguments:
      <element1> <element2> ...: One or more elements to be reversed.
    Example: python main.py reverse-array apple banana cherry  # Returns ['cherry', 'banana', 'apple']
"""
    print(help_message)


def main(args: List[str]):
    """
    Main function to parse command-line arguments and dispatch to appropriate
    utility functions.

    Args:
        args (List[str]): A list of command-line arguments, including the script name.
    """
    if len(args) < 2:
        display_help()
        sys.exit(1)

    command = args[1].lower()

    if command == "add":
        if len(args) != 4:
            print("Error: Usage for 'add': python main.py add <num1> <num2>", file=sys.stderr)
            sys.exit(1)
        try:
            num1 = float(args[2])
            num2 = float(args[3])
            result = add(num1, num2)
            print(result)
        except ValueError:
            print("Error: Both arguments for 'add' must be valid numbers.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred during 'add' command: {e}", file=sys.stderr)
            sys.exit(1)

    elif command == "convert":
        if len(args) < 3 or len(args) > 4:
            print("Error: Usage for 'convert': python main.py convert <value> [unit]", file=sys.stderr)
            sys.exit(1)
        try:
            value = float(args[2])
            # Default unit is Celsius if not provided
            unit = args[3].upper() if len(args) == 4 else 'C' 

            if unit == 'C':
                converted_value = celsius_to_fahrenheit(value)
                print(f"{value}°C is {converted_value}°F")
            elif unit == 'F':
                converted_value = fahrenheit_to_celsius(value)
                print(f"{value}°F is {converted_value}°C")
            else:
                print("Error: Invalid unit for 'convert'. Use 'C' or 'F'.", file=sys.stderr)
                sys.exit(1)
        except ValueError:
            print("Error: Temperature value must be a valid number.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred during 'convert' command: {e}", file=sys.stderr)
            sys.exit(1)

    elif command == "reverse-array":
        if len(args) < 3:
            print(
                "Error: Usage for 'reverse-array': python main.py reverse-array <element1> <element2> ...",
                file=sys.stderr
            )
            sys.exit(1)
        
        # All arguments from index 2 onwards are considered elements of the array
        elements = args[2:]
        try:
            reversed_elements = reverse_array(elements)
            print(reversed_elements)
        except Exception as e:
            print(f"An unexpected error occurred during 'reverse-array' command: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        print(f"Error: Unknown command '{command}'.", file=sys.stderr)
        display_help()
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)