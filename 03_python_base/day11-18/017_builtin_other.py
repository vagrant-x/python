print("=============内置函数=========")

# 内置函数
# 	进制转换 bin oct hex int
# 	符号和序值转换 chr ord
# 	数学运算类 divmod pow round abs
# 	执行字符串 eval exec
# 	判断类 all any
# 	对象简单操作 hash len id
# 	对象高级操作 zip max min sorted
# 	多数值输出 dir locals vars
# 	其他 help isinstnce  __import__

# bin oct hex
# bin
# 将一个integer对象转换为 binary
print(bin(8))  # 0b1000

# oct
# 将一个integer 转换为 octal
print(oct(10))  # 0o12

# hex
# 将一个integer 转换为 hexadecimal
print(hex(17))  # 0x11

# 将其他进制的数据转换为 10进制
print(int(0x10ffff))  # 1114111

# chr
# 根据序值返回对应的 Unicode的字符
print(chr(97))  # a

# ord
print(ord("a"))  # 97

# divmod
# 返回一个元组，元组为 (x//y, x%y)， 第一个元素是整数商，第二个是余数
print(divmod(10, 3))  # (3, 1)

# pow
print(pow(2, 3))  # x**y 结果：8
print(pow(2, 3, 5))  # x**y % z 结果：3
print("-----------------------")

# round
# 四舍五入
print(round(3.4))  # 3
print(round(3.5))  # 4

# sum
# 用于计算数字值类型的数字总和
print(sum([1, 2, 3]))  # 6

"""
    sum 和 reduce
    sum 用于计算数字值类型的数字总和
    reduce 通过两个参数的函数，从左到右累加的应用于序列的项，将序列缩减为单个值。
    reduce 可以通过设置函数实现更强大的功能
"""

# abs
# 返回参数的绝对值
print(abs(10))  # 10
print(abs(-10))  # 10

# eval
#
"""
一、函数的作用

将字符串str当成有效的表达式来求值并返回计算结果。它要执行的python代码只能是单个运算表达式（不支持任意形式的赋值操作），而不能是复杂的代码逻辑。

二、函数的定义

eval(expression, globals=None, locals=None)

参数说明：

expression：必选参数，可以是字符串，也可以是一个任意的code对象实例（可以通过compile函数创建）。如果它是一个字符串，它会被当作一个python表达式进行分析和解释。

globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。

locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与globals相同的值。

如果globals与locals都被忽略，那么它们将取eval()函数被调用环境下的全局命名空间和局部命名空间。

返回值：

如果expression是一个code对象，且创建该code对象时，compile函数的mode参数是’exec’，那么eval()函数的返回值是None

否则，如果expression是一个输出语句，如print()，则eval()返回结果为None

否则，expression表达式的结果就是eval()函数的返回值

"""
# 计算字符串中的表达式，并返回结果
print(eval("pow(2,2)"))  # 4

# 将字符串转换成对象(list dict tuple 与字符串的转换)
print(type(eval("[1,2]")))  # <class 'list'>
print(type(eval("{'a':1}")))  # <class 'dict'>
print(type(eval("(1,2)")))  # <class 'tuple'>

# 更改不同域的变量值
x = 10


def test_eval():
    y = 20
    a = eval("x + y")
    print("a = {}".format(a))
    b = eval("x + y", {"x": 1, "y": 2})  # globals 指定
    print("b = {}".format(b))
    c = eval("x + y", {"x": 2, "y": 3}, {"y": 4, "z": 5})  # globals locals 都指定
    print("c = {}".format(c))


test_eval()
print("x = {}".format(x))
# 结果：
#     a = 30
#     b = 3
#     c = 6

# exec
"""
一、函数的作用

执行存储在字符串或文件中的python语句

二、函数的定义

exec(expression, globals=None, locals=None)

参数说明：

object：必选参数，表示需要被指定的 Python 代码。它必须是字符串或 code 对象。如果 object 是一个字符串，该字符串会先被解析为一组 Python 语句，然后再执行（除非发生语法错误）。如果 object 是一个 code 对象，那么它只是被简单的执行。
globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与 globals 相同的值。

返回值：
    exec 返回值永远为None
"""

# 执行单语句字符串
exec("print('test exec')")  # test exec

# 执行多语句字符串
exec("""for i in range(5): print('i = {}'.format(i))""")
# 结果：
#     i = 0
#     i = 1
#     i = 2
#     i = 3
#     i = 4

# 结合 globals locals
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""


def test_exec():
    y = 20
    exec(expr)  # 60
    exec(expr, {"x": 1, "y": 2})  # 33
    exec(expr, {"x": 1, "y": 2}, {"y": 3, "z": 4})  # 34


test_exec()

"""
eval 和 exec 的区别
    eval 函数将字符串当成python表达式来求值，并返回计算结果
    exec 函数将字符串当成python表达式或是代码块来执行，不返回计算结果

"""

# all
# 如果可迭代对象 所有元素 bool(x) 都是 True，返回 True。 如果可迭代对象为空，返回 True
print(all([]))  # True
print(all([1, 2, 0]))  # False

# any
# 对可迭代对象所有元素执行 bool(x) 如果一个为True ，返回True。如果可迭代对象为空，返回False
print(any([]))  # False
print(any(["", [], {}, ()]))  # False
print(any(["", [], {}, (), 1]))  # True

# hash
# 在一次程序运行期间，相同的字符串（不可变对象）其hash值是一样的
# 可hash 的数据类型即不可变数据类型，不可hash 的数据类型即可变数据类型
print(hash("12345"))

# len
# 返回一个对象的长度
print(len("abc"))

# id
# 返回一个对象的唯一标识，这保证了同时存在的对象是唯一的
print(id(1))  # 140727915537040
print(id(1) == id(1))  # True

# zip
"""
zip
    将可迭代对象作为参数，将对象中的元素按照顺序打包成元组，返回这些元组组成的一个可迭代对象。
    如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
"""
z = zip(["a", "b", "c"], [1, 2, 3])
print(z)  # <zip object at 0x00000204207FFFC8>
print(list(z))  # [('a', 1), ('b', 2), ('c', 3)]
print(*zip("abc", [1, 2, 3], ("A", "B", "C")))  # ('a', 1, 'A') ('b', 2, 'B') ('c', 3, 'C')

# max min
# max
"""
max
    函数功能为取传入的多个参数中的最大值，或者传入的可迭代对象元素中的最大值。
    默认数值型参数，取值大者；字符型参数，取字母表排序靠后者。
    参数key，其为一个函数，用来指定取最大值的方法。
    default命名参数用来指定最大值不存在时返回的默认值.

    # 不同类型之间不能进行比较啊
"""
# 简单求列表中的最大值
print(max([1, 23, 4, 99, 10]))  # 99

# 求指定对象的最大值
age_dic = {'a1_age': 18, 'a2_age': 20, 'c1_age': 100, 'b3_age': 300}
print(max(age_dic))  # c1_age

# 设置求最大值方法
print(max(age_dic, key=lambda i: age_dic[i]))  # b3_age

# min
# 简单求列表中的最小值
print(min([1, 23, 4, 99, 10]))  # 1

# 求指定对象的最小值
age_dic = {'a1_age': 18, 'a2_age': 20, 'c1_age': 100, 'b3_age': 300}
print(min(age_dic))  # a1_age

# 设置求最小值方法
print(min(age_dic, key=lambda i: age_dic[i]))  # a1_age

# repr
# 把对象转换为字符串
print(repr({"a": 1}))

# sorted
"""
sorted
    sorted(iterable, key=None, reverse=False)  
        iterable -- 可迭代对象。
        key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
        reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
    返回值： 重新排序的列表


"""
# 没有设置key的排序
print(sorted([2, 3, 5, 6, 1]))  # [1, 2, 3, 5, 6] 默认升序

#
d = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(sorted(d))  # [1, 2, 3, 4, 5]
print(sorted(d, key=lambda x: d[x]))  # [5, 2, 3, 1, 4]

"""
sort 与 sorted 区别：
    sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
"""
l1 = [1, 2, 6, 3]
l2 = [1, 2, 6, 3]
l1.sort()
print(l1)  # [1, 2, 3, 6] 改变原来的值
print(sorted(l2))  # [1, 2, 3, 6] 没有改变原来的值，生成一个新的list
print(l2)  # [1, 2, 6, 3]

# dir
# 如果没有参数，返回作用域中的名称
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# 安装字母顺序返回对象的属性，如果对象提供了 __dir__ 则使用它，否则使用默认的 dir()
print(dir(1))
# ['__abs__', '__add__', ......,  'numerator', 'real', 'to_bytes']


# locals
# 返回一个包含当前域所有变量的字典
print(locals())  # { '__name__': '__main__', '__doc__': None,'x': 10,  'i': 4, ......}

# vars
# 返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。
test_vars = "test_vars"
print(vars())  # {'__name__': '__main__', '__doc__': None,  ...... , 'test_vars': 'test_vars'}

# help
# 输出帮助信息
# print(help(str))


print("""""isinstance""")
# isinstnce
# 判断一个对象是否值给定数据类型的实例， 数据类型可以是一个元组
print(isinstance("abc", str))  # True
print(isinstance(1, (int, str)))  # True
print(isinstance((1,), (int, str)))  # False

# __import__
"""
    __import__() 函数用于动态加载类和函数 。如果一个模块经常变化就可以使用 __import__() 来动态载入。
    加载获取到的模块名是字符串的情况
"""
print(__import__("functools"))  # <module 'functools' from 'E:\\0000_Python_3.7.3\\lib\\functools.py'>
