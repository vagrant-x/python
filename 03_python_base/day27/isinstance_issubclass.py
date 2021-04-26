"""
isinstance
    判断某个对象是不是某个类的实例
"""
class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, A))  # True
print(isinstance(b, B))  # True


"""
issubclass
    判断某个类是不是另一个类的子类
"""
class A:
    pass

class B(A):
    pass

print(issubclass(B, A))  # True
print(issubclass(B, object))  # True
print(issubclass(B, type))   # False



