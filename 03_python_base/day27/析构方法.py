"""
__del__
    析构方法：对象在内存中被释放时，自动触发执行。
    注意：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关系内存的分配和释放，
    因为此做一般交给Python解释器来执行，所以，析构函数的调用是由解释器在进行垃圾回收是自动触发执行的。

"""
class Student:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("调用了__del__")


s = Student("xu")
del s
print("执行完成之前释放")

s1 = Student("xu1")
print("程序到此结束")

# 结果：
#     调用了__del__
#     执行完成之前释放
#     程序到此结束
#     调用了__del__
