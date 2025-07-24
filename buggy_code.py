# buggy_code.py

def calculate_sum(a, b):
    # Fixed syntax error: added missing right parenthesis
    print("Calculating sum for", a, b)
    return a + b

def divide_numbers(x, y):
    # Check for valid numeric types
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "Error: Both arguments must be numeric"
    
    # Check for division by zero
    if y == 0:
        return "Error: Cannot divide by zero"
    
    # Perform the division
    result = x / y
    return result

if __name__ == "__main__":
    # 测试 calculate_sum
    try:
        sum_result = calculate_sum(10, 5)
        print(f"Sum: {sum_result}")
    except Exception as e:
        print(f"Unexpected error in calculate_sum: {e}")

    # 测试 divide_numbers
    try:
        div_result = divide_numbers(10, 0) # 故意制造除零错误
        print(f"Division: {div_result}")
    except Exception as e:
        print(f"Unexpected error in divide_numbers (zero division): {e}")

    try:
        div_result_type_error = divide_numbers(10, "hello") # 故意制造类型错误
        print(f"Division with type error: {div_result_type_error}")
    except Exception as e:
        print(f"Unexpected error in divide_numbers (type error): {e}")