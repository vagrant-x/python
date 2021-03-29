if __name__ == '__main__':
    test = "abc"
    print(test.ljust(10, "*"))  # 返回指定长度的左对齐字符串，使用指定填充符（默认是空格） ：abc*******
    print(test.rjust(10, "*"))  # ：*******abc
    print(test.zfill(10))  # 根据给定长度，在左边填充0到指定长度 ：0000000abc

    str = "username\temail\tpassword\nxu1\txu1@qq.com\t123\nxu1\txu1@qq.com\t123\nxu1\txu1@qq.com\t123"
    expandtabs_str = str.expandtabs(20)  # 返回制表符扩展到指定长度的副本，如果没有指定，默认是8
    print(expandtabs_str)

    print("".isalnum())  # False
    print("1212aaa".isalnum())  # True
    print("1212-aa".isalnum())  # False

    print("shi".isalpha())  # True
    print("是".isalpha())  # True
    print("12".isalpha())  # False

    #decimal 十进制的 小数的
    #digit n.	(从 0 到 9 的任何一个)数字
    print("②".isdecimal())  # False
    print("②".isdigit())  # True
    print("2".isdecimal())  # True
    print("2".isdigit())  # True
    print("二".isdecimal())  # False
    print("二".isdigit())  # False
# ====================================================================

# 如果字符串所有字符都可以打印，返回True，否则返回False
#     print("abc\tdef".isprintable())  # 有制表符，返回 False'

# 如果字符串至少有一个字符并且都是空白格，返回True，否则返回False
    print("".isspace())  # False
    print("1   ".isspace())  # False
    print(" ".isspace())  # True

# istitle: 判断是否是标题格式，每个单词首字母大写
# title: 将字符串转换为标题格式
    test = "Python version 3"
    print(test.istitle())  # False
    test1 = test.title()
    print(test1)  # Python Version 3
    print(test1.istitle())  # True

# 对传入的可迭代对象，对象的元素是字符串的，将元素拼接并在中间插入指定字符串；返回拼接对象
    print("_".join("abcd"))  # a_b_c_d
    print("_".join(("1", "2", "3",)))  # 1_2_3
    print("_".join(["1", "2", "3"]))  # 1_2_3

# 判断字符串是否全部是大写 或  小写（至少包含一个字符的字符串）
    print("aaa".islower())  # True
    print("AAa".islower())  # False
    print("AAA".isupper())  # True
    print("AAa".isupper())  # False
# 将字符串转换为大写 或  小写
    print("aaa".upper())  # AAA
    print("AAA".lower())  # aaa

# 如果给定字符串，则移除字符串, 注意：会尽可能多的进行匹配
    test = "1212312314"
    print(test.lstrip("12"))  # [312314]
    print(test.lstrip("123"))  # [4]
# 去除左右空白
    test = "   1231234   "
    print(test.lstrip())   # [1231234   ]
    print(test.rstrip())  # [   1231234]
    print(test.strip())  # [1231234]
# 去除 \t \n
    test = "123123\t"
    print(test.strip())  # [123123]
    test = "123123\n"
    print(test.strip())  # [123123]

# maketrans ： 生成一个转换表(dict对象)给str.translate() 使用，如果传入一个参数，应该是一个dict,
# 如果传入两个参数，两个参数的长度需要一样长
# translate: 根据转换表替换给定字符串中匹配的字符到指定字符
    test = "abcabcabcdefdefdef"
    mt = str.maketrans("adf", "123")  # 创建转换规则, 输出为 {97: 49, 100: 50, 102: 51}
    print(test.translate(mt))  # 1bc1bc1bc2e32e32e3

# 根据给定表示对字符串进行分割，返回一个长度魏三的元组：
# 元组的第一部分是分割标识前面的字符串
# 第二部分是分隔符自身
# 第三部分是发现的第一个分隔符后面的部分
    print("aabccbddbeebdd".partition("b"))  # ('aa', 'b', 'ccbddbeebdd')
    print("aabccbddbeebdd".rpartition("b"))  # 从右边进行分割： ('aabccbddbee', 'b', 'dd')

# 根据分隔符进行分割，如果没事设置分割数量，则将字符串都进行分割，并用列表返回
    print("aabccbddbeebbdd".split("b"))  # ['aa', 'cc', 'dd', 'ee', '', 'dd']
    print("aabccbddbeebbdd".split("b", 2))  # ['aa', 'cc', 'ddbeebbdd']

# 根据换行符进行分割，False： 不包含换行符，True： 包含换行符
    print("aaa\nbbb\nccc".splitlines(False))  # ['aaa', 'bbb', 'ccc']
    print("aaa\nbbb\nccc".splitlines(True))  # ['aaa\n', 'bbb\n', 'ccc']

# 将字符串中字符大小写转换
    print("AbCd".swapcase())  # aBcD

# #如果字符串是有效标识符，则 isidentifier() 方法返回 True，否则返回 False。
# #如果字符串仅包含字母数字字母（a-z）和（0-9）或下划线（_），则该字符串被视为有效标识符。有效的标识符不能以数字开头或包含任何空格
    print("def1".isidentifier())  # True

# 根据替换字符串中的子序列，如果没有给定替换数量，将替换所有
    print("abcabcdede".replace("abc", '123', 1))  # 123abcdede

# ====================================================================
# 1 for 循环
    print("===============================================")
    for c in "abc":
        print(c)
    # a
    # b
    # c

# 2 索引（下标）获取字符串中某一个字符
    print("abc"[1])  # b
    # print("abc"[4])  # IndexError: string index out of range

# 3 切片
    print("abcd123"[1:2])  # b
    print("abcd123"[1:-1])  # bcd12
    print("abcd123"[1:-2])  # bcd1
    print("abcd123"[1:])  # bcd123

# 4 获取长度
    print(len("123"))  # 3

#5 获取连续或是等步长的数字
# Python2中直接创建在内容中 ;python3中只有for循环时，才一个一个创建
    print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]