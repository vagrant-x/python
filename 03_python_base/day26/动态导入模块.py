# 动态导入模块


# 导入 m1/t.py module_t 实际上是指向到m1
module_t = __import__("m1.t")
print(module_t)  # <module 'm1' from '/home/a5673/xuzj/05_code/python_base/03_python_base/day26/m1/__init__.py'>
module_t.t.test1()  # m1 -> t.py : test1()


# 通过 import * 模块中带下划线的方法将不被导入
from m1.t import *
test1()  # m1 -> t.py : test1()
test2()  # m1 -> t.py : test2()
_test3()  # NameError: name '_test3' is not defined


from m1.t import test1, test2, _test3
test1()  # m1 -> t.py : test1()
test2()  # m1 -> t.py : test2()
_test3()  # m1 -> t.py : _test3()

# 通过 importlib 导入
import importlib
m = importlib.import_module("m1.t")
print(m)  # <module 'm1.t' from '/home/a5673/xuzj/05_code/python_base/03_python_base/day26/m1/t.py'>
m.test1()  # m1 -> t.py : test1()
