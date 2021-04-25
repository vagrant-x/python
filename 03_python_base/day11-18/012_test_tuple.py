if __name__ == '__main__':
    # tuple 元组，一级元素不可被修改，不能被增加或者删除

#===================方法====================
    tuple
    t = (11, 22, 33, 44)
    print(type(t))
# 返回第一个出现的索引，如果值不存在，抛出 ValueError
    print(t.index(22, 0, -1))  # 1

# 返回查询元素出现的次数
    t = (11, 22, 33, 44, 22)
    print(t.count(22))  # 2

#===================操作====================
    # 索引操作
    t = ("a", "b", "c", "d", "e")
    print(t[2])  # c

    # 切片操作
    t = ("a", "b", "c", "d", "e")
    print(t[2: 4])  # ('c', 'd')

    # for 循环
    for item in t:
        print(item)
    # 结果：
    #     a
    #     b
    #     c
    #     d
    #     e

    # 转换
    # 字符串和元组相互转换
    s = "abcde"
    print(tuple(s))  # ('a', 'b', 'c', 'd', 'e')
    print("".join(('a', 'b', 'c', 'd', 'e')))  # abcde
    # 列表和元组相互转换
    print(tuple(["a", 1, True]))  # ('a', 1, True)
    print(list(("a", 1, True)))  # ['a', 1, True]


