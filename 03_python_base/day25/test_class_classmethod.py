"""
classmethod
    当我们需要和类直接进行交互，而不需要和实例进行交互时，类方法是最好的选择。
    类方法与实例方法类似，但是传递的不是类的实例，而是类本身，
    第一个参数是cls。我们可以用类的实例调用类方法，也可以直接用类名来调用。
"""
class A:
    class_attr = "attr"

    @classmethod
    def class_foo(cls):
        print("classmethod -> attr:{}".format(cls.class_attr))

# 类直接调用类方法
A.class_foo()  # classmethod -> attr:attr
# 实例化调用类方法
a = A()
a.class_foo()  # classmethod -> attr:attr

"""
@staticmethod
    staticmethod 装饰器也会改变方法的调用方式， 但是第一个参数不是特殊的值。
    其实， 静态方法就是普通的函数， 只是碰巧在类的定义体中， 而不是在模块层定义。
    可以实现实例化使用 C().f()，当然也可以不实例化调用该方法 C.f()。
    
    静态方法类似普通方法，参数里面不用self。
    这些方法和类相关，但是又不需要类和实例中的任何信息、属性等等。
    如果把这些方法写到类外面，这样就把和类相关的代码分散到类外，使得之后对于代码的理解和维护都是巨大的障碍。
    而静态方法就是用来解决这一类问题的。
"""

# 检查是否开启了日志功能，这个和类相关，但是跟类的属性和实例都没有关系。
log_enabled = True
class B:
    class_attr = "attr"

    @staticmethod
    def static_foo():
        if log_enabled:
            print("log is enabled")
        else:
            print("log is disabled")

B.static_foo()  # log is enabled