class Lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print("===> Lazypropertt.__get__ 参数: instance = {}, owner = {}".format(instance, owner))
        if instance is None:
            return self
        res = self.func(instance)
        setattr(instance, self.func.__name__, res)
        return self.func(instance)

    # def __set__(self, instance, value):
    #     pass


class Room:

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    # @property  # area=property(area)
    @Lazyproperty  # # area=Lazyproperty(area)
    def area(self):
        return self.width * self.height

#  @property 测试代码
# r = Room("房间", 2, 3)
# print(Room.__dict__)  # {..., 'area': <property object at 0x7f8b42de5ea8>,}
# print(r.area)  # 6

# r2 = Room("房间2", 2, 3)
# print(r2.__dict__)  # {'name': '房间2', 'width': 2, 'height': 3}
# print(r2.area)

# print(Room.area)  # <__main__.Lazyproperty object at 0x7faabd589a58>

r3 = Room("房间3", 2, 3)
print(r3.area)
print(r3.area)
# 结果（只计算一次）：
#     ===> Lazypropertt.__get__ 参数: instance = <__main__.Room object at 0x7fd98e3757b8>, owner = <class '__main__.Room'>
#     6
#     6