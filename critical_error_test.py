# critical_error_test.py

# 1. 致命语法错误：函数定义缺少冒号，导致程序无法解析并启动
def startup_killer_syntax_error(param1, param2)
    print("This line will never be reached.")
    return param1 + param2

# 2. 运行时错误：未处理的除零，直接导致程序终止
def guaranteed_runtime_crash():
    result = 10 / 0 # 这行代码在运行时必然抛出 ZeroDivisionError
    print(f"This result is: {result}") # 这行也不会被执行

# 3. 强制触发的索引错误：访问不存在的列表索引
def guaranteed_index_crash():
    my_list = [1, 2, 3]
    value = my_list[100] # 这行代码在运行时必然抛出 IndexError
    print(f"Value: {value}") # 这行也不会被执行

# 4. 导入错误：导入一个不存在的模块，导致程序启动失败
# import non_existent_module_for_test

if __name__ == "__main__":
    print("Starting critical error test...")

    # 如果要测试语法错误，取消注释下面这行。这将导致整个脚本无法运行。
    # startup_killer_syntax_error(1, 2)

    # 如果要测试未处理的运行时错误，取消注释下面这行。
    # 程序会在调用该函数时崩溃。
    # guaranteed_runtime_crash()

    # 或者测试索引错误
    # guaranteed_index_crash()

    # 或者测试导入错误 (如果你的 BugBot 检查包括模块导入)
    # import non_existent_module_for_test

    print("Test finished (if code reached here).") # 这行可能不会被打印出来
    print("Test finished (if code reached here).") # 这行可能不会被打印出来
    print("Test finished (if code reached here).") # 这行可能不会被打印出来