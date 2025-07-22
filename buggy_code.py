# buggy_code.py

def calculate_sum(a, b):
    # Fixed syntax error: added missing closing parenthesis
    print("Calculating sum for", a, b)
    return a + b

def divide_numbers(x, y):
    # Check for type errors
    try:
        # Attempt to convert to float to handle numeric strings
        x = float(x)
        y = float(y)
    except (TypeError, ValueError):
        return "Error: Both arguments must be numeric"
    
    # Check for zero division
    if y == 0:
        return "Error: Cannot divide by zero"
    
    # Perform the division
    result = x / y
    return result

if __name__ == "__main__":
    # 测试 calculate_sum
    sum_result = calculate_sum(10, 5)
    print(f"Sum: {sum_result}")

    # 测试 divide_numbers
    # Test normal division
    div_result_normal = divide_numbers(10, 2)
    print(f"Division 10/2: {div_result_normal}")
    
    # Test zero division
    div_result = divide_numbers(10, 0) # 故意制造除零错误
    print(f"Division by zero: {div_result}")

    # Test type error
    div_result_type_error = divide_numbers(10, "hello") # 故意制造类型错误
    print(f"Division with type error: {div_result_type_error}")