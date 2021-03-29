print("test global and nonlocal")

#一、 全局变量 和 局部变量
"""
局部变量：定义在函数内部的变量称为局部变量，他的作用域范围为函数内，也就是出了函数外就无效。
        全局变量是位于模块文件内部的顶层的变量名
        全局变量如果是在函数内被赋值的话，必须经过声明
        全局变量名在函数内部不经过声明也可以被引用
全局变量：定义在函数外的变量称之为全局变量，他的作用域范围为全局。
"""


# 二、global 和 nonlocal
# 2.1======= global ===============


# 如果函数的内容无 global 关键字
    # 有声明局部变量
    # 使用方法内的变量
NAME = ["xu1", "xu2"]
def pName():
    NAME = "xu"
    print("name is ", NAME)  # 使用的是局部声明的变量
pName()  # name is  xu

    # 如果无生命局部变量
    # 方法内没声明变量，到方法外找，找到全局变量，使用全局变量
NAME = ["xu1", "xu2"]
def pName():
    NAME.append("xu3")
    print("name is ", NAME)  # 使用的是全局声明的变量
pName()  # name is  ['xu1', 'xu2', 'xu3']

# 如果函数的内容有 global 关键字
    # 有声明局部变量
    #使用方法内的变量
NAME = ["xu1", "xu2"]
def pName():
    NAME = "XU"
    print("name is ", NAME)
pName()  # name is  XU
print(NAME)  # ['xu1', 'xu2']

# 声明了局部变量，不能在引入全局变量
# def pName():
#     NAME = "XU"
#     global NAME  # SyntaxError: name 'NAME' is assigned to before global declaration
#     print("name is ", NAME)
# pName()  # 报错

    # 无声明局部变量
    # 通过global 声明全局变量，使用全局变量
NAME = ["xu1", "xu2"]
def pName():
    global NAME
    NAME = ["XU"]
    print("name is ", NAME)
pName()  # name is  ['XU']
print(NAME)  # ['XU']

# 全局变量 和 局部变量的命名规则
# 全局变量名大写， 局部变量名小写  进行区分

# 总结：
# 方法作用域内优先读取局部变量，能读取全局变量，无法对全局变量重新赋值；但是对于可变类型，可以对内部元素进行操作
# 如果函数中有 global关键字，变量本质上就是全局的那个变量，可以读取可以赋值。

print("____________________")
# 2.2 nonlocal
# 指定上一级变量，如果没有就继续往上找，直到找到为止
# nonlocal 列出的变量必须在上一层定义过，否之将报错,其查找的作用域仅为嵌套的def
NAME = "XU1"
name1 = "11"
def pName():
    NAME = "xu2"
    def p1Name():
        # nonlocal NAME, name1  # def 内没有声明name1 报错
        nonlocal NAME
        NAME = "xu3"
    p1Name()
    print(NAME)
print(NAME)
pName()
print(NAME)