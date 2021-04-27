class Mytype(type):
    def __init__(self, a, b, c):
        print("===》 执行元类构造方法")
        print("===》 元类__init__ 第一个参数：{}".format(self))
        print("===》 元类__init__ 第二个参数：{}".format(a))
        print("===》 元类__init__ 第三个参数：{}".format(b))
        print("===》 元类__init__ 第四个参数：{}".format(c))

    def __call__(self, *args, **kwargs):
        print("=====》 执行元类__call__方法")
        print("=====》 元类__call__ args：{}".format(args))
        print("=====》 元类__call__ kwargs：{}".format(kwargs))
        obj = object.__new__(self)  # object.__new__(Student)
        self.__init__(obj, *args, **kwargs)  # Student.__init__(s, *args, **kwargs)
        return obj


class Student(metaclass=Mytype):  # Student=Mytype(Student, "Student", (), {}) ---> __init__
    def __init__(self, name):
        self.name = name  # s.name=name

print("Student类：{}".format(Student))
s = Student("xu")
print("实例：{}".format(s))

# 结果：
#     ===》 执行元类构造方法
#     ===》 元类__init__ 第一个参数：<class '__main__.Student'>
#     ===》 元类__init__ 第二个参数：Student
#     ===》 元类__init__ 第三个参数：()
#     ===》 元类__init__ 第四个参数：{'__module__': '__main__', '__qualname__': 'Student', '__init__': <function Student.__init__ at 0x00000269BCA9A670>}
#     Student类：<class '__main__.Student'>
#     =====》 执行元类__call__方法
#     =====》 元类__call__ args：('xu',)
#     =====》 元类__call__ kwargs：{}
#     实例：<__main__.Student object at 0x00000269BC9E8400>