# buggy_code.py

def calculate_sum(a, b):
    # 故意引入一个语法错误：缺少右括号
    print("Calculating sum for", a, b)
    return a + b
def divide_numbers(x, y):
    # 修正：处理除数为零的情况
    if y == 0:
        return "Error: Cannot divide by zero"

    # 修正：执行除法运算
    result = x / y
    return f"The result is: {result}" # 返回一个格式化的字符串，包含结果

if __name__ == "__main__":
    # 测试 calculate_sum
    sum_result = calculate_sum(10, 5)
    print(f"Sum: {sum_result}")

    # 测试 divide_numbers
    print("\n--- Division Tests ---")
    div_result_ok = divide_numbers(10, 2)
    print(f"10 / 2: {div_result_ok}")

    div_result_zero = divide_numbers(10, 0) # 仍故意制造除零错误，看看是否会返回错误字符串
    print(f"10 / 0: {div_result_zero}")