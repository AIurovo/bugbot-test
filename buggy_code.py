# buggy_code.py

def calculate_sum(a, b):
    """Calculate the sum of two numbers with input validation."""
    # Fix Bug 3: Add input validation for type safety
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric (int or float)")
    
    print("Calculating sum for", a, b)
    return a + b

def divide_numbers(x, y):
    """Divide two numbers with proper error handling."""
    # Fix Bug 2: Use exceptions instead of returning different types
    # Check for valid numeric types
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numeric (int or float)")
    
    # Check for division by zero
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    # Perform the division
    result = x / y
    return result

if __name__ == "__main__":
    # Test calculate_sum with proper error handling
    try:
        sum_result = calculate_sum(10, 5)
        print(f"Sum: {sum_result}")
    except (TypeError, ValueError) as e:
        print(f"Sum error: {e}")

    # Test divide_numbers with proper error handling
    try:
        div_result = divide_numbers(10, 0)  # Will raise ZeroDivisionError
        print(f"Division: {div_result}")
    except ZeroDivisionError as e:
        print(f"Division error: {e}")
    except TypeError as e:
        print(f"Division type error: {e}")

    try:
        div_result_type_error = divide_numbers(10, "hello")  # Will raise TypeError
        print(f"Division with type error: {div_result_type_error}")
    except TypeError as e:
        print(f"Division type error: {e}")
    except ZeroDivisionError as e:
        print(f"Division error: {e}")
    
    # Fix Bug 1: Remove duplicate print statements - demonstrate successful division
    try:
        div_result_success = divide_numbers(10, 2)
        print(f"Successful division: {div_result_success}")
    except (TypeError, ZeroDivisionError) as e:
        print(f"Division error: {e}")