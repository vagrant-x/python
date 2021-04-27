class Descriptors:

    def __init__(self, key, value_type):
        self.key = key
        self.value_type = value_type

    def __get__(self, instance, owner):
        print("===> 执行Descriptors的 get")
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print("===> 执行Descriptors的 set")
        if not isinstance(value, self.value_type):
            raise TypeError("参数%s必须为%s" % (self.key, self.value_type))
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print("===>  执行Descriptors的delete")
        instance.__dict__.pop(self.key)


class Person:
    name = Descriptors("name", str)
    age = Descriptors("age", int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("xu", 15)
print(person.__dict__)
person.name
person.name = "xu-1"
print(person.__dict__)
# 结果：
#     ===> 执行Descriptors的 set
#     ===> 执行Descriptors的 set
#     {'name': 'xu', 'age': 15}
#     ===> 执行Descriptors的 get
#     ===> 执行Descriptors的 set
#     {'name': 'xu-1', 'age': 15}


class Descriptors:
    def __get__(self, instance, owner):
        print("===> 执行 Descriptors get")

    def __set__(self, instance, value):
        print("===> 执行 Descriptors set")

    def __delete__(self, instance):
        print("===> 执行 Descriptors delete")


class University:
    name = Descriptors()

    def __init__(self, name):
        self.name = name


# 类属性 > 数据描述符
# 在调用类属性时，原来字典中的数据描述法被覆盖为 XX-XX
print(University.__dict__)  # {..., 'name': <__main__.Descriptors object at 0x7ff8c0eda278>,}

University.name = "XX-XX"
print(University.__dict__)  # {..., 'name': 'XX-XX',}


# 数据描述符 > 实例属性
# 调用时会现在实例里面找，找不到name属性，到类里面找，在类的字典里面找到 'name': <__main__.Descriptors object at 0x7fce16180a58>
# 初始化时调用 Descriptors 的 __set__； un.name 调用  __get__
print(University.__dict__)
un = University("xx-xx")
un.name
# 结果：
#     {..., 'name': <__main__.Descriptors object at 0x7ff8c0eda278>,}
#     ===> 执行 Descriptors set
#     ===> 执行 Descriptors get




class Descriptors:
    def __get__(self, instance, owner):
        print("===>2 执行 Descriptors get")


class University:
    name = Descriptors()

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print("---> 查找 item = {}".format(item))

# 实例属性 > 非数据描述符
# 在创建实例的时候，会在属性字典中添加 name，后面调用 un2.name 访问，都是访问实例字典中的 name
un2 = University("xu2")
print(un2.name)  # xu    并没有调用到  Descriptors 的 __get__
print(un2.__dict__)  # {'name': 'xu2'}
un2.name = "xu-2"
print(un2.__dict__)  # {'name': 'xu-2'}

# 非数据描述符 > 找不到的属性触发__getattr__
# 找不到 name1 使用 __getattr__
un3 = University("xu3")
print(un3.name1)  # ---> 查找 item = name1

