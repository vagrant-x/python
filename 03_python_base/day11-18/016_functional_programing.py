# ================= 函数式编程 ========================
"""
高阶函数  - 高阶函数
    Functional Programming, 函数式编程。
    满足两个特性任意一个即为高阶函数
        (1)函数传入参数是一个函数名
        (2)函数返回值是一个函数名
"""

# 函数作为参数传入另一个函数
def bar():
    print("func: bar")
def foo(func):
    print("func: foo")
    func()
foo(bar)
# 结果：
#     func: foo
#     func: bar

# 函数作为另一个函数的返回值
def bar():
    print("func: bar")
def foo():
    print("func: foo")
    return bar
b = foo()
b()
# 结果：
#     func: foo
#     func: bar


# ================= 函数式编程 ========================