"""
__str__
    print() str() 调用的都是 __str__ 方法

"""

class Persion:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Persion('name' = {}, 'age' = {})".format(self.name, self.age)

p = Persion("xu", 100)
print(p)  # Persion('name' = xu, 'age' = 100)

p_str = str(p)
print(p_str)  # Persion('name' = xu, 'age' = 100)

p__str__ = p.__str__()
print(p__str__)  # Persion('name' = xu, 'age' = 100)


"""
__repr__
    在交互式时解释器会使用该方法

>>> class Persion:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...     def __repr__(self):
...         return "repr:  Persion('name' = {}, 'age' = {})".format(self.name, self.age)
...
>>> p = Persion("xu", 99)
>>> p
repr:  Persion('name' = xu, 'age' = 99)
>>>

"""


class Persion:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Persion('name' = {}, 'age' = {})".format(self.name, self.age)

    def __repr__(self):
        return "repr:  Persion('name' = {}, 'age' = {})".format(self.name, self.age)


p = Persion("xu", 100)
print(p)  # Persion('name' = xu, 'age' = 100)

p_repr = repr(p)
print(p_repr)  # repr:  Persion('name' = xu, 'age' = 100)

"""
总结：
    str() 或是 print() 调用 obj.__str__()
    repr() 或者交互式解释器调用 obj.__repr__()
    如果 __str__ 没有被定义，那么就是使用 __repr__ 来代替输出
    注意：两个方法返回值必须时字符串，否则抛出异常
"""
