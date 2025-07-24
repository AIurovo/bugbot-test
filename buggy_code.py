# buggy_code.py

def calculate_sum(a, b):
    # Fixed syntax error: added missing right parenthesis
    print("Calculating sum for", a, b)
    # Ensure both inputs are numeric types
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric")

    return a + b

def divide_numbers(x, y):
    # Check for valid numeric types
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numeric")
    
    # Check for division by zero
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    # Perform the division
    result = x / y
    return result

if __name__ == "__main__":
    # Test calculate_sum
    try:
        sum_result = calculate_sum(10, 5)
        print(f"Sum: {sum_result}")
    except TypeError as e:
        print(f"Sum calculation failed: {e}")

    # Test divide_numbers with zero divisor
    try:
        div_result = divide_numbers(10, 0)
        print(f"Division: {div_result}")
    except (TypeError, ZeroDivisionError) as e:
        print(f"Division failed: {e}")

    # Test divide_numbers with invalid type
    try:
        div_result_type_error = divide_numbers(10, "hello")
        print(f"Division with type error: {div_result_type_error}")
    except (TypeError, ZeroDivisionError) as e:
        print(f"Division failed: {e}")