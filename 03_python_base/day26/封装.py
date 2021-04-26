"""
封装
    隐藏对象的属性和实现细节，对外提供公共访问方式。
    好处：将变化隔离，提高安全性
    原则：
        1、将不需要对外提供的内容隐藏起来
        2、把属性都隐藏，提供公共方法对其访问

"""
class Room:
    def __init__(self, name, owner, width, length):
        self.name = name
        self.owner = owner
        self.__width = width
        self.__length = length

    def cal_area(self):
        return self.__length * self.__width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            print("传入数据类型不对")
        elif width < 0:
            print("宽度必须大于0")
        else:
            self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if not isinstance(length, int):
            print("传入数据类型不对")
        elif length < 0:
            print("长度必须大于0")
        else:
            self.__length = length


room = Room("r001", "xu", 10, 10)
print(room.cal_area())  # 100
room.width = 20
room.length = 20
print(room.cal_area())  # 400
