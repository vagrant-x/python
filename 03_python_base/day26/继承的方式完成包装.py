# 继承的方式完成包装： 继承+ 派生
# 继承现有类，重写部分方法
class ListStr(list):
    def append(self, p_object):
        if type(p_object) is str:
            super().append(p_object)
        else:
            print("只能添加字符串类型元素")

l = ListStr("abc")
print(l)  # ['a', 'b', 'c']
l.append("12")
print(l)  # ['a', 'b', 'c', '12']
l.append(12)
print(l)  # ['a', 'b', 'c', '12']

"""

授权：
    授权是包装的一个特性，包装一个类型通常是对已存在的类型的一些定制。
    这种做法可以新建、修改或删除原有产品的功能。其他的则保持原样。
    授权的过程，即是所有更新的功能都是新类的某部分来处理，但已存在的功能就授权给对象的默认属性

组合的方式完成授权：
    需求：对文件进行写操作时，再写入每一行内容之前添加时间
"""
import time

class FileHandle:
    def __init__(self, filename, mode='r', encoding="utf-8"):
        self.file = open(filename, mode, encoding=encoding)
        self.mode = mode
        self.encoding =encoding

    # 通过 getattr 调用原来已存在的功能
    # f.read 先去对象里面找，找不到再去类里找， 找不到调用此方法
    def __getattr__(self, item):
        return getattr(self.file, item)

    # 重写 write 方法
    def write(self, line):
        time_str = time.strftime("%Y-%m-%d %X")
        self.file.write("{} {}".format(time_str, line))

f = FileHandle("a.txt", "r+")
f.write("这是写入的内容")
f.flush()  # 将内容写入硬盘
f.seek(0)  # 文件内光标移动到第一行开始文字
line1 = f.read()  # 读取文件
print(line1)  # 2021-04-26 21:07:41 这是写入的内容