# bug_showcase.py

import os  # Bug 1: 未使用的导入 (Unused import) - 很多工具会报告

# Bug 2: 全局变量与局部变量混淆 (Global vs Local scope confusion)
global_counter = 0


def increment_counter():
    # 尝试修改全局变量，但没有使用 global 关键字，会导致创建一个同名的局部变量
    counter = global_counter + 1  # 实际上是创建了局部变量counter
    print(f"Inside function, local counter: {counter}")
    return counter


def calculate_average(numbers):
    # Bug 3: 空列表的除零风险 (ZeroDivisionError risk for empty list)
    # Bug 4: 浮点数精度问题在求和时可能累积 (Floating point precision)
    total = 0.0
    for num in numbers:
        total += num

    # Bug：如果 numbers 为空，len(numbers) 为0，这里会抛出 ZeroDivisionError
    return total / len(numbers)


def find_item(data_list, target):
    # Bug 5: 循环内修改列表导致跳过元素 (Modifying list during iteration)
    # 假设我们想删除所有目标元素
    for item in data_list:
        if item == target:
            data_list.remove(item)  # Bug：在迭代时修改列表，会跳过紧接着的元素
    return data_list


def check_password(password):
    # Bug 6: 硬编码密码 (Hardcoded password) - 严重安全问题
    if password == "admin123":  # 密码硬编码在代码中
        print("Access granted!")
        return True
    else:
        print("Access denied!")
        return False


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Bug 7: 缺少 __eq__ 方法 (Missing __eq__ for value comparison)
    # 导致两个内容相同的User对象，如果不是同一个实例，会判断不相等
    # 例如：User("Alice", 30) == User("Alice", 30) 默认返回 False
    pass


def process_data(data):
    # Bug 8: 未处理的异常 (Unhandled exception) - 潜在的 KeyError 或 TypeError
    value = data["key"]  # 假设 'key' 总是存在，如果不存在则会抛出 KeyError
    print(f"Processed value: {value}")
    return value


# 主执行块
if __name__ == "__main__":
    print("--- Counter Test ---")
    print(f"Initial global counter: {global_counter}")
    increment_counter()
    print(f"After increment_counter, global counter: {global_counter}")  # 期望是1，实际是0

    print("\n--- Average Calculation Test ---")
    scores = [90, 85, 92, 78]
    print(f"Average of {scores}: {calculate_average(scores)}")
    empty_list = []
    print(f"Average of empty list: {calculate_average(empty_list)}")  # 期望 BugBot 警告此处

    print("\n--- Item Finding Test ---")
    numbers = [1, 2, 3, 2, 4, 2, 5]
    print(f"Original list: {numbers}")
    modified_numbers = find_item(numbers, 2)
    print(f"Modified list after removing 2s: {modified_numbers}")  # 期望：并非所有2都被移除

    print("\n--- Password Check Test ---")
    check_password("userpass")
    check_password("admin123")  # 期望 BugBot 警告硬编码密码

    print("\n--- User Object Comparison Test ---")
    user1 = User("Bob", 25)
    user2 = User("Bob", 25)
    print(f"Are user1 and user2 equal (by content)? {user1 == user2}")  # 期望 BugBot 提示 __eq__

    print("\n--- Data Processing Test ---")
    valid_data = {"key": 100}
    process_data(valid_data)
    invalid_data = {"another_key": 200}
    # BugBot 应该能发现这里传入 invalid_data 时，访问 'key' 会导致 KeyError
    # process_data(invalid_data) # 如果执行，会直接崩溃