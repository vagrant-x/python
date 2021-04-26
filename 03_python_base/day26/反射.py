"""
实例化对象的反射操作
"""


class A:
    country = "China"
    area = "guangzhou"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        return "call func return"


a = A("xu", 100)

print(hasattr(a, "name"))  # True

# 一般 hasattr 与 getattr 结合起来使用
if hasattr(a, "name"):
    print(getattr(a, "name"))  # xu

# 可以设置一个默认值，目的是防止程序报错； 如果没有该属性，就返回默认值
print(getattr(a, "sex", None))

fun1 = getattr(a, "func")
print(fun1())  # call func return

# 给对象设置属性
setattr(a, "sex", "男")
print(a.__dict__)  # {'name': 'xu', 'age': 100, 'sex': '男'}
print(a.sex)  # 男


"""
类名的反射操作
"""


class A:
    country = "China"
    area = "guangzhou"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        return "call func return"

# 获取类A的静态属性country
print(getattr(A, "country"))  # China
# 获取类A 的func 方法并执行
print(getattr(A, "func")(None))  # call func return
