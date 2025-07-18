def divide_numbers(dividend: float, divisor: float):
    """Divide two numbers and handle division by zero.

    If the divisor is zero, return the string "Error: Division by zero" instead of raising
    an exception, keeping parity with previous in-code expectations.

    Args:
        dividend (float): The numerator of the division.
        divisor (float): The denominator of the division.

    Returns:
        float | str: The result of the division, or an error message if divisor is zero.
    """
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return "Error: Division by zero"


# The following function previously claimed to contain a syntax error, which was inaccurate.
# The comment has been updated to reflect the correct status of the function.

def calculate_sum(numbers):
    """Calculate the sum of an iterable of numbers.

    Args:
        numbers (Iterable[float]): An iterable containing numeric values.

    Returns:
        float: The sum of all numbers in the iterable.
    """
    total = 0
    for number in numbers:
        total += number
    return total