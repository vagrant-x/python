# """
# 继承：
#     在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
#     新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
#
#
# 继承最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，
# 因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
# """
# class Animal:
#     def run(self):
#         print("Animal is running...")
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# d = Dog()
# d.run()   # Animal is running...
#
# # 当然，也可以对子类增加一些方法，比如Dog类：
# # 继承的第二个好处需要我们对代码做一点改进。你看到了，无论是Dog还是Cat，它们run()的时候，显示的都是Animal is running...，符合逻辑的做法是分别显示Dog is running...和Cat is running...，因此，对Dog和Cat类改进如下：
#
# class Dog(Animal):
#     def run(self):
#         print("Dog is running ...")
#
#     def eat(self):
#         print("Eating meat")
#
# class Cat(Animal):
#     def run(self):
#         print("cat is running ...")
#
# d = Dog()
# d.run()  # Dog is running ...
#
#
# # 判断是否是继承类的实例
# print(isinstance(d, Animal))  # True
# print(isinstance(d, Dog))  # True


# """
# 接口继承：
#     接口继承实质上是要求“做出一个良好的抽象”，这个抽象规定一个兼容接口，是的外部调用者无需关心具体细节，
#     可一视同仁的处理实现了特定接口的所有对象。———— 这个程序设计上，叫归一化
#
# """
# import abc
#
# # 定义一个抽象接口的类
# class All_file(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def read(self):
#         ellipsis
#
#     @abc.abstractmethod
#     def write(self):
#         pass
#
# # 继承抽象接口类并实现其抽象方法
# class Disk(All_file):
#
#     def read(self):
#         print("disk 实现 read 抽象方法")
#
#     def write(self):
#         print("disk 实现 write 抽象方法")
#
# d = Disk()
# d.read()  # disk 实现 read 抽象方法
# d.write()  # disk 实现 write 抽象方法


# class A:
#     def test(self):
#         print("test -> A")
#
# class B:
#     def test(self):
#         print("test -> B")
#
# class C(A, B):
#     pass
#
# C().test()  # test -> A


"""
super
    通过super调用父类方法

"""


class Vehicle:
    countey = "china"

    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print("开动了")


class Subway(Vehicle):
    def __init__(self, name, speed, load, power, line):
        super().__init__(name, speed, load, power)
        self.line = line

    def run(self):
        super().run()
        print("{} {} 线开始启动".format(self.name, self.line))

    def show_info(self):
        print(self.name, self.speed, self.load, self.power, self.line)

l = Subway("广州地铁", "60km/h", 1000, "电", "3")
l.show_info()  # 广州地铁 60km/h 1000 电 3
l.run()
# 开动了
# 广州地铁 3 线开始启动