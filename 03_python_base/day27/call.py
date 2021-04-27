"""
__call__

    该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用。

    Python 中，凡是可以将 () 直接应用到自身并执行，都称为可调用对象。可调用对象包括自定义的函数、Python 内置函数以及本节所讲的类实例对象。
    对于可调用对象，实际上“名称()”可以理解为是“名称.__call__()”的简写。
"""
class CLanguage:

    # 定义__call__ 方法
    def __call__(self, *args, **kwargs):
        print("调用 __call__ 方法， 参数： args = {}, kwargs = {}".format(args, kwargs))

c = CLanguage()
# 通过在 CLanguage 类中实现 __call__() 方法，使的 clangs 实例对象变为了可调用对象。
c("测试对象c")  # 调用 __call__ 方法， 参数： args = ('测试对象c',), kwargs = {}
c.__call__("直接使用call")  # 调用 __call__ 方法， 参数： args = ('直接使用call',), kwargs = {}


"""
通过函数直接调用call
"""
def info(*args, **kwargs):
    print("打印信息： args = {}, kwargs = {}".format(args, kwargs))

info("直接调用")  # 打印信息： args = ('直接调用',), kwargs = {}
info.__call__("call调用")  # 打印信息： args = ('call调用',), kwargs = {}


"""
用 __call__() 弥补 hasattr() 函数的短板
    前面章节介绍了 hasattr() 函数的用法，该函数的功能是查找类的实例对象中是否包含指定名称的属性或者方法，但该函数有一个缺陷，即它无法判断该指定的名称，到底是类属性还是类方法。
    要解决这个问题，我们可以借助可调用对象的概念。要知道，类实例对象包含的方法，其实也属于可调用对象，但类属性却不是。
"""
class CLanguage:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("这是一门： {}".format(self.name))


cl = CLanguage("pyhton")
if hasattr(cl, "name"):
    print(hasattr(cl.name, "__call__"))  # False
if hasattr(cl, "info"):
    print(hasattr(cl.info, "__call__"))  # True
