
"""
__len__() 方法
    这里假如要计算实例化对象a 的属性个数，
    直接使用 len(a)将报 TypeError: object of type 'A' has no len()， 类没有 len() 方法
    在类A 内部添加 __len__ 方法， 可以成功获取到长度
    通过这个例子可以得知，那些能使用 len()的数据类型内部实现 __len__方法
"""
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        return len(self.__dict__)

a = A("xu", 100)
print(len(a))  # 2


"""
__str__ 方法
    对一个对象打印是，自动执行 __str__ 方法
    没有实现 __str__ 时返回： <__main__.A object at 0x7fcfecfb0a20>
"""
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        res = "A{ "
        for k in self.__dict__:
            res += str(k) + ": " + str(getattr(self, k)) + ", "
        res += " }"
        return res

a =A("xu", 100)  # A{ name: xu, age: 100,  }
print(a)


"""
__call__ 方法
    调用实例化对象时自动触发 __call__ 方法
"""
class A:
    def __init__(self, name, age):
        print("实例化一个对象时执行 __init__ 方法")
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print("调用实例化对象时自动触发 __call__ 方法: args = {}, kwargs = {}".format(args, kwargs))

a = A("xu", 99)  # 实例化一个对象时执行 __init__ 方法
a()  # 调用实例化对象时自动触发 __call__ 方法: args = (), kwargs = {}


"""
__new__ 构造方法
    实例化一个对象是，发送了三件事：
        1、在内存中开辟一个对象空间，obj(即a)中 __new__ 开辟的
        2、自动执行 __init__ 方法，将空间传给 self
        3、在 __init__ 给对象封装属性，并返回给对象
    也就是说，实例化一个对象的时候，首先执行 __new__ 方法， 然后执行 __init__ 方法
"""
class A:
    def __init__(self, name, age):
        print("实例化一个对象时执行 __init__ 方法")
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("实例化一个对象时执行 __new__ 方法")
        return object.__new__(cls)

a = A("xu", 98)


"""
__new__ 实现单例模式
    单例模式： 一个类只能实例化一个对象
"""
class A:
    __instance = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a1 = A("xu1", 101)
a2 = A("xu2", 202)

print(a1)  # <__main__.A object at 0x7f2868fe9c18>
print(a2)  # <__main__.A object at 0x7f2868fe9c18>
print("a1  name = {}, age = {}".format(a1.name, a1.age))  # a1  name = xu2, age = 202
print("a2  name = {}, age = {}".format(a2.name, a2.age))  # a2  name = xu2, age = 202

"""
item 系列
    __getitem__
    __setitem__
    __delitem__
"""
class A:

    def __init__(self, name, age):
        self.name = name
        self.age = age
# -----------------------------

    def __getitem__(self, item):
        print("---> getitem: {}".format(item))
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print("---> setitem: key ={}, value = {}".format(key, value))
        self.__dict__[key] = value

    def __delitem__(self, key):
        print("---> delitem: {}".format(key))
        self.__dict__.pop(key)

# -----------------------------
    def __getattr__(self, item):
        print("===> getattr: {}".format(item))
        return self.__dict__[item]

    def __setattr__(self, key, value):
        print("===> setattr: key = {}, vaule = {}".format(key,value))
        self.__dict__[key] = value

    def __delattr__(self, item):
        print("===> delattr: {}".format(item))
        self.__dict__.pop(item)

a = A('xu', 97)
# ===> setattr: key = name, vaule = xu
# ===> setattr: key = age, vaule = 97

a["age"] = 20  # ---> setitem: key =age, value = 20
a["age1"] = 21  # ---> setitem: key =age1, value = 21
a['age']  # ---> getitem: age
del a['age1']  # ---> delitem: age1

a.age = 31  # ===> setattr: key = age, vaule = 31
a.age1 = 32  # ===> setattr: key = age1, vaule = 32
a.age  #
a.age2  # ===> getattr: age2 调用获取对象的属性不存在的时候才会执行
del a.age1  # ===> delattr: age1
