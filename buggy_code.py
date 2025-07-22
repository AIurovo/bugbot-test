# buggy_code.py

def calculate_sum(a, b):
    # 故意引入一个语法错误：缺少右括号
    print("Calculating sum for", a, b)
    return a + b

def divide_numbers(x, y):
    # 类型和零除检查
    # 1. 类型检查 - 仅允许 int 或 float
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "Error: Both inputs must be numbers"

    # 2. 零除检查
    if y == 0:
        return "Error: Cannot divide by zero"

    # 3. 执行除法并返回结果
    return x / y

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