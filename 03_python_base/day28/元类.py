"""
元类

1、python 中一切皆是对象，类本身也是一个对象，当使用关键字 class 的时候，python 解释器在加载 class 的时候会创建一个对象（这里的对象指的是类而非类的实例）

"""
class Student:
    pass

s = Student()
print(type(s))  # <class '__main__.Student'>
print(type(Student))  # <class 'type'>

"""
2、什么是元类
    元类是类的类，是类的模板
    元类是用来控制如何创建类的，正如类是创建对象的模板一样
    元类的实例为类，正如类的实例为对象。
    type 是python 的一个内建元类，用来直接控制生成类，python中任何 class 定义的类其实是 type 类实例化的对象

3、创建类的两种方法：

"""
# 方法一
class Student:
    def info(self):
        print("---> student info")

# 方法二
def info(self):
    print("---> student info")

Student = type("Student", (object,), {"info": info, "x": 1})

"""
4、一个类没有声明自己的元类，默认其元类是 type, 除了使用元类 type, 用户也可以通过继承 type 来自定义元类
"""