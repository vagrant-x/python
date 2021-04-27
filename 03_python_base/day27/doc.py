"""
__doc__
    查看说明文档
    要写#这种注释不要写到def方法内要写到它的上面位置和装饰器类似，相反三引号'''不要写到def外面,这样也是没显示效果的。
    help() 函数底层也是借助 __doc__ 属性实现的
"""
class Student:
    """
        Student 类： 没有说明
    """

    tag = "a0001"

    def __init__(self, name, age):
        """
        初始化方法
        :param name: 名字
        :param age: 年龄
        """
        self.name = name
        self.age = age

    def info(self):
        """
        打印学生信息
        :return:
        """
        print("这是一个学生：name = {}, age = {}".format(self.name, self.age))

    # 没有内部说明
    def info2(self):
        # 里面不生效
        pass


s = Student("xu", 97)
print(Student.__doc__)  # Student 类： 没有说明
print(Student.info.__doc__)  # 打印学生信息  :return:

help(Student)
