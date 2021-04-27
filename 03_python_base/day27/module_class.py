"""
__module__ 和 __class__

__module__ 查看类或是创建对象的类所在的模块
__class__ 查看创建对象的类名
"""

from m1.t1 import Test

print(Test.__module__)  # m1.t1
print(Test.__class__)  # <class 'type'>

t = Test()
print(t.__module__)  # m1.t1
print(t.__class__)  # <class 'm1.t1.Test'>