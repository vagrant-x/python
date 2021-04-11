"""
一个 .py 文件称之为一个模块（module）

使用模块的好处：
    提高代码的可维护性；
    方便其他地方引用，减少重复代码
    避免函数名和变量名冲突；相同名字的函数和变量可以分别存放在不同的模块中

模块一共三种：
    python标准库
    第三方模块
    应用程序自定义模块

"""

"""
模块的导入方法
    import 语句
    from ... import 语句
    from ... import * 语句
    运行本质 & sys.path
"""
"""
    import 语句 
        （1）通过 import 导入模块的时候，解释器通过 sys.path 里面的路径去寻找模块
        （2）如果当前目录下存在与要引入模块同名的文件，就会屏蔽要引入的模块
        

"""
import time
import sys
# 等同于
# import time, sys


# 测试引入自定义与标准同名模块
"""
# re.py 内容
def findall(*args):
    return "自定义 findall"
"""
import re
print(re.findall(r"aa", "ccbabaa"))  # 如果使用标准的re模块，返回 ['aa']， 存在同名re模块，返回 "自定义 findall", 标准模块被屏蔽

# from ... import 语句
# 将某个模块中的部分变量引入到当前模块中
from os import getpid, getppid
print("pid = {}, ppid = {}".format(getpid(), getppid()))  # pid = 16224, ppid = 12072


#from ... import * 语句
# 引入一个模块中定义的所有项目。尽量少使用这种引用方法，有可能出现同名覆盖的情况

# 模块内定义了一个time函数，导入标准time模块的所有方法，自定义的time被覆盖
def time():
    return "自定义time"
print(time())  # 自定义time
from time import *
print(time())  # 1618105888.3513176

# 运行本质
import module_test1
# 结果：
#     module_test1 -> add
#     module_test1 -> sub
#     module_test1 -> mul
#     module_test1 -> finish
## 导入 module_test1 模块的时候，会从头到尾先执行整个文件

from module_test1 import add
# 结果:
#     module_test1 -> add
#     module_test1 -> sub
#     module_test1 -> mul
#     module_test1 -> finish
## 从模块中导入一个定义的函数或变量，也会从头到尾执行整个模块，再将指定的模块引入当前模块

"""
包（package）
    包（package）：按照目录组织模块的方法。
    比如：存在两个同名模块abc,我们可以通过包来组织模块，将两个同名模块放到不同的包中，通过指定包名来引入指定的模块
    请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录(文件夹)，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是对应包的名字。
"""

from pk1 import abc as abc1
from pk2 import abc as abc2
abc1.print_abc()  # pk1 -> abc
abc2.print_abc()  # pk2 -> ab





# sys.path
# 如果执行 pk3.pk3_test 里面的代码，是没有办法直接引用到上一层目录下的 module_test1.py 模块，因为sys.path 里面的所有路径下找不到该模块
# 需要将整个模块的路径添加到sys.path, 这样就可以引用到
# 代码在 pk3_test.py

# __name__ 参数
"""
    如果执行某个py文件的时候，当前的__name__ 是 "__main__"
    如果模块是通过import引入的，其__name__ 的值将是文件名
"""
print(__name__)  # __main__
import re
print(re.__name__)  # re
