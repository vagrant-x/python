if __name__ == '__main__':
    s1 = "abcde"
    s2 = "a1b2c3d4"
    S1 = "ABCDE"
    S2 = "A1B2C3D4"

    # test = "aLex"
    # 首字母大写
    # v = test.capitalize()
    # print(v)
    print("abcde".capitalize())  # 把首字母大写 :Abcde

    # 所有变小写，casefold更牛逼，很多未知的对相应变小写
    # v1 = test.casefold()
    print("ABCDE".casefold())  # 所有字母变小写，功能比lower强大，很多未知的相应变小写 :abcde
    # print(v1)
    # v2 = test.lower()
    print("ABCDE".lower())  # 所有字母变小写：abcde
    # print(v2)

    # 设置宽度，并将内容居中
    # 20 代指总长度
    # *  空白未知填充，一个字符，可有可无
    # v = test.center(20,"中")
    print("abc".center(10, "*"))  # 以字符串为中心，两边用填充字符补齐到设定长度 ：***abc****
    # print(v)

    # 去字符串中寻找，寻找子序列的出现次数
    # test = "aLexalexr"
    # v = test.count('ex')
    print("abcABCabABa".count("ab"))  # 计算子序列出现的次数: 2
    print("abcABCabABa".count("ab", 3, 11))  # 从位置为3到位置11寻找子序列出现的次数 1
    # print(v)

    # test = "aLexalexr"
    # v = test.count('ex',5,6)
    # print(v)

    # 欠
    # encode
    # decode

    # 以什么什么结尾
    # 以什么什么开始
    # test = "alex"
    # v = test.endswith('ex')
    print("abcde".startswith("ab"))  # 判断是否以ab 开始: True
    # v = test.startswith('ex')
    print("abcde".endswith("de"))  # 判断是否以de 结束： True
    # print(v)

    # 欠
    # test = "12345678\t9"
    # v = test.expandtabs(6)
    # print(v,len(v))

    # 从开始往后找，找到第一个之后，获取其未知
    # > 或 >=
    # test = "alexalex"
    # 未找到 -1
    # v = test.find('ex')
    print("python".find("on"))  # 寻找子序列所在的位置(找到返回起始位置，否则返回-1)：4
    # print(v)

    # index找不到，报错   忽略
    # test = "alexalex"
    # v = test.index('8')
    print("python".index("py"))  # 寻找子序列起始位置，找到返回起始位置序号，否则报错
    # print(v)



    # 格式化，将一个字符串中的占位符替换为指定的值
    # test = 'i am {name}, age {a}'
    # print(test)
    # v = test.format(name='alex',a=19)
    # print(v)


    # test = 'i am {0}, age {1}'
    # print(test)
    # v = test.format('alex',19)
    # print(v)

    # 格式化，传入的值 {"name": 'alex', "a": 19}
    # test = 'i am {name}, age {a}'
    # v1 = test.format(name='df',a=10)
    # v2 = test.format_map({"name": 'alex', "a": 19})

    # 格式化，将一个字符串中的占位符替换为指定的值
    print("i am {name}, age {num}".format(name="python", num=9))  # i am python, age 9
    print("i am {0}, age {1}".format("python", 9))  # i am python, age 9
    print("i am {name}, age {num}".format_map({"name": "python", "num": 9}))  # i am python, age 9

    # 字符串中是否只包含 字母和数字
    # test = "123"
    # v = test.isalnum()
    # print(v)
    # print("test str")

    print("aaa".isalnum())  # 字符串是否只包含 字母和数字： True
    print("aaa111_".isalnum())  # False
