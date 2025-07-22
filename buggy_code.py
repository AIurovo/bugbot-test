# buggy_code.py

def calculate_sum(a, b):
    # 故意引入一个语法错误：缺少右括号
    print("Calculating sum for", a, b
    return a + b

def divide_numbers(x, y):
    # Check if y is zero
    if isinstance(y, (int, float)) and y == 0:
        return "Error: Cannot divide by zero"
    # Check if both x and y are numbers
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "Error: Both arguments must be numbers"
    result = x / y
    return f"The result is: {result}"

if __name__ == "__main__":
    # 测试 calculate_sum
    sum_result = calculate_sum(10, 5)
    print(f"Sum: {sum_result}")

    # 测试 divide_numbers
    div_result = divide_numbers(10, 0) # 故意制造除零错误
    print(f"Division: {div_result}")

    div_result_type_error = divide_numbers(10, "hello") # 故意制造类型错误
    print(f"Division with type error: {div_result_type_error}")
    print(f"Division with type error: {div_result_type_error}")
    print(f"Division with type error: {div_result_type_error}")