"""
描述符 + 类装饰器

"""
class Typed:
    def __init__(self, key, type):
        self.key = key
        self.type = type

    def __get__(self, instance, owner):
        print("---> get 方法")
        # print("instance = {}, owner = {}".format(instance, owner))
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print("---> set 方法")
        # print("instance = {}, value = {}".format(instance, value))
        if not isinstance(value, self.type):
            # print("设置name的值不是字符串： type = {}".format(type(value)))
            # return
            raise TypeError("设置{}的值不是{},当前传入数据的类型是{}".format(self.key, self.type, type(value)))
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print("---> delete 方法")
        # print("instance = {}".format(instance))
        instance.__dict__.pop(self.key)


def deco(**kwargs):
    def wrapper(obj):
        for k, v in kwargs.items():
            setattr(obj, k, Typed(k, v))
        return obj
    return wrapper


@deco(name=str, age=int)
class Person:
    # name = Typed("name", str)
    # age = Typed("age", int)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = Person("xu", 99, 100.0)
print(Person.__dict__)
print(p1.__dict__)
p1.name = "XU1"
print(p1.__dict__)
del p1.name
print(p1.__dict__)
# 结果：
#     ---> set 方法
#     ---> set 方法
#     {..., 'name': <__main__.Typed object at 0x7f3d79729dd8>, 'age': <__main__.Typed object at 0x7f3d79729e48>}
#     {'name': 'xu', 'age': 99, 'salary': 100.0}
#     ---> set 方法
#     {'name': 'XU1', 'age': 99, 'salary': 100.0}
#     ---> delete 方法
#     {'age': 99, 'salary': 100.0}
