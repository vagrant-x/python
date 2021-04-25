print("test str")
# Python的字符串格式化有两种方式：百分号方式 和 format方式
#百分号的方式相对来说比较老，
# format方式则是相对比较先进，企图替换古老的方式，目前两者都支持。



#1 百分号

"""

    (name)      可选，用于选择指定的key
    flags          可选，可供选择的值有:
        +       右对齐；正数前加正好，负数前加负号；
        -        左对齐；正数前无符号，负数前加负号；
        空格    右对齐；正数前加空格，负数前加负号；
        0        右对齐；正数前无符号，负数前加负号；用0填充空白处
    width         可选，占有宽度
    .precision   可选，小数点后保留的位数
    typecode    必选
        s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
        r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
        c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
        o，将整数转换成 八  进制表示，并将其格式化到指定位置
        x，将整数转换成十六进制表示，并将其格式化到指定位置
        d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
        e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
        E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
        f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
        F，同上
        g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
        G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）
        %，当字符串中存在格式化标志时，需要用 %%表示一个百分号

"""

#1.1 通过位置传参
# %[(name)][flags][width].[precision]typecode

msg = "i am %s, my hobby is %s" % ("xu", 'conding')
print(msg)  # i am xu, my hobby is conding

# %s打印数据类型
#   可以打印数字, 列表, 字典
msg = "i am %s, my hobby is %s" % ("xu", 1)  # i am xu, my hobby is 1
print(msg)
msg = "i am %s, my hobby is %s" % ("xu", [1, 2])  # i am xu, my hobby is [1, 2]
print(msg)
msg = "i am %s, my hobby is %s" % ("xu", {"a": "a"})  # i am xu, my hobby is {'a': 'a'}
print(msg)

# 打印浮点数
f = "percent %.2f" % 99.123456789
print(f)  # percent 99.12

# 打印带百分号， %%
f = "percent %.2f%%" % 99.123456789
print(f)  # percent 99.12%

# 1.2 通过关键字传参
msg = "i am %(name)s age %(age)d" % {"name": "xu", "age": 18}
print(msg)  # i an xu age 18

# flags：对齐
# width: 占有宽度
# 右对齐
msg = "i am %(name)+10s age %(age)d" % {"name": "xu" , "age": 18}
print(msg)  # i am         xu age 18
# 左对齐
msg = "i am %(name)-10s age %(age)d" % {"name": "xu" , "age": 18}
print(msg)  # i am xu         age 18


# 2 format 方式
# [[fill]align][sign][#][0][width][,][.precision][type]
print("test format")
"""

    fill           【可选】空白处填充的字符
    align        【可选】对齐方式（需配合width使用）
        <，内容左对齐
        >，内容右对齐(默认)
        ＝，内容右对齐，将符号放置在填充字符的左侧，且只对数字类型有效。 即使：符号+填充物+数字
        ^，内容居中
    sign         【可选】有无符号数字
        +，正号加正，负号加负；
         -，正号不变，负号加负；
        空格 ，正号空格，负号加负；
    #            【可选】对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示
    ，            【可选】为数字添加分隔符，如：1,000,000
    width       【可选】格式化位所占宽度
    .precision 【可选】小数位保留精度
    type         【可选】格式化类型
        传入” 字符串类型 “的参数
            s，格式化字符串类型数据
            空白，未指定类型，则默认是None，同s
        传入“ 整数类型 ”的参数
            b，将10进制整数自动转换成2进制表示然后格式化
            c，将10进制整数自动转换为其对应的unicode字符
            d，十进制整数
            o，将10进制整数自动转换成8进制表示然后格式化；
            x，将10进制整数自动转换成16进制表示然后格式化（小写x）
            X，将10进制整数自动转换成16进制表示然后格式化（大写X）
        传入“ 浮点型或小数类型 ”的参数
            e， 转换为科学计数法（小写e）表示，然后格式化；
            E， 转换为科学计数法（大写E）表示，然后格式化;
            f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
            F， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
            g， 自动在e和f中切换
            G， 自动在E和F中切换
            %，显示百分比（默认显示小数点后6位）

"""

# 参数的数据类型
# key=value 的形式
f = "i am {name}, age {age}"
fs = f.format(name="xu", age=18)
print(fs)  # i am xu, age 18

# 列表的形式
f = "i am {:s}, age {:d}"
fs = f.format(*["xu", 19])
print(fs)  # i am xu, age 19

# 字典的形式
f = "i am {name}, age {age}"
fs = f.format(**{"name": "xu", "age": 17})
print(fs)  # i am xu, age 17

# 不同数据类型打印
f = "numbers: {:b}, {:o}, {:d}, {:x}, {:X}, {:%}"
fs = f.format(15, 15, 15, 15, 15, 15.123456789)
print(fs)  # numbers: 1111, 17, 15, f, F, 1512.345679%

f = "numbers: {num:b}, {num:o}, {num:d}, {num:x}, {num:X}, {num1:%}"
fs = f.format(num=15, num1=15.123456)
print(fs)  # numbers: 1111, 17, 15, f, F, 1512.345600%


# 2.2 传参的方式
# 按照位置传参（默认）
f = "i am {}, age {}"
fs = f.format("xu", 11)
print(fs)  # i am xu, age 11

print("___________________")
# 按照位置传参（指定位置参数）
f = "i am {0}, age {1}, really {0}"
fs = f.format("xu", 12)
print(fs)  # i am xu, age 12, really xu

# 按照关键字传参
f = "i am {name}, age {age}"
fs = f.format(name="xu", age=18)
print(fs)  # i am xu, age 18

# 按照参数属性
class Point:
     def __init__(self, x, y):
         self.x, self.y = x, y
     def __str__(self):
         return 'Point({self.x}, {self.y})'.format(self=self)
print(Point(4, 2))  # Point(4, 2)

# 通过属性的元素
coord = (3, 5)
f = "X : {0[0]}, Y: {0[1]}"
fs = f.format(coord)
print(fs)  # X : 3, Y: 5

# 参数打印格式化，以关键字传参为例
# 左对齐字符串
f = "i am {name:<10s}, age{age}"
fs = f.format(name="xu", age=18)
print(fs)  # i am xu        , age18

# 添加数字分隔符， 保留2位小数
f = "number: {count:,.2f}"
fs = f.format(count=2123123123)
print(fs)  # number: 2,123,123,123.00

# 设置填充字符和对齐方式
f = "number: {count:=>10}"
fs = f.format(count=2123123)
print(fs)  # number: ===2123123

# 百分号
f = "Correct answers:{:.2%}".format(19/22)
print(f)  # Correct answers:86.36%

# 按照不同进制格式化数据
f = "int: {0:d}, hex:{0:x}, oct:{0:o}, bin:{0:b}"
fs = f.format(42)
print(fs)  # int: 42, hex:2a, oct:52, bin:101010
f = "int: {0:#d}, hex:{0:#x}, oct:{0:#o}, bin:{0:#b}"
fs = f.format(42)
print(fs)  # int: 42, hex:0x2a, oct:0o52, bin:0b101010

# 格式化时间
import datetime
d = datetime.datetime(2021, 3, 29, 12, 27, 30)
f = "{:%Y-%m-%d %H:%M:%S}"
print(f.format(d))  # 2021-03-29 12:27:30
