#!/usr/bin/env python
# -*- coding:utf-8 -*-

if __name__ == '__main__':
# =======================列表============================
# list

#1 append 在列表末尾添加对象
    li = [1, 2, 3]
    print(li.append("a"))  # None
    print(li)  # [1, 2, 3, 'a']
#2  clear 清空列表所有项目
    print(li.clear())  # None
    print(li)  # []

#3copy 浅拷贝 返回一个浅拷贝的列表
    li = ["a", "b", "c"]
    libak = li.copy()  # ['a', 'b', 'c']
    print(libak)

# 4 返回指定元素出现的次数
    li = ["a", "b", "c"]
    print(li.count("a"))  # 1

# 5 extend 迭代对象，扩展list
    li = ["a", "b", "c"]
    li.extend("123")
    print(li)  # ['a', 'b', 'c', '1', '2', '3']

#6 index 返回第一个查找元素的索引，如果查找元素不存在则报错
    li = [11, 22, 33, 22, 44]
    print(li.index(22))  # 1
    # print(li.index(223))  # ValueError: 223 is not in list

    print("+++++++++++++++")
# 7 insert 将对象插入到索引前面
    li = [11, 22, 33, 22, 44]
    li.insert(1, "aa")
    print(li)  # [11, 'aa', 22, 33, 22, 44]

# 8 pop 删除并返回指定索引的元素，如果没有指定索引，默认最后一个, 如果列表为空或是超出范围，将报 IndexError
    li = [11, 22, 33, 22, 44]
    print(li.pop())  # 44
    print(li)  # [11, 22, 33, 22]
    li = [11, 22, 33, 22, 44]
    print(li.pop(0))  # 11
    print(li)  # [22, 33, 22, 44]

# 9 remove 删除第一个出现的元素，如果元素不存在，报 ValueError
# 删除的操作 pop remove clear     del li[0]    del li[2:4]
    li = [11, 22, 33, 22, 44]
    li.remove(22)
    print(li)  # [11, 33, 22, 44]
    li = [11, 22, 33, 22, 44]
    del li[0]
    print(li)  #

# 10 reverse 将列表反转
    li = [11, 22, 33, 22, 44]
    li.reverse()
    print(li)  # [44, 22, 33, 22, 11]

# 11 sort 按照升序排序并且返回None
    li = [11, 44, 22, 33, 22]
    li.sort(reverse=True)
    print(li)  # [44, 33, 22, 22, 11]


# ===================================================
# 1 列表的元素可以是数字、字符串、列表、布尔值、列表、字典等等,列表的值可以被修改（元组的一级元素不可以）
# 2 索引取值
    # 查询
    li = [11, 22, 33, 22, 44]
    print(li[1])  # 22
    # 修改
    li[1] = "aa"
    print(li)  # [11, 'aa', 33, 22, 44]
    # 删除
    li = [11, 22, 33, 22, 44]
    del li[1]
    print(li)  # [11, 33, 22, 44]

# 3 切片
    # 查询
    li = [11, 22, 33, 22, 44]
    print(li[1:3])  # [22, 33]
    # 修改
    li = [11, 22, 33, 22, 44]
    li[1: 4] = ["aa"]
    print(li)  # [11, 'aa', 44]
    # 删除
    li = [11, 22, 33, 22, 44]
    del li[2: 4]
    print(li)  # [11, 22, 44]


# 4 for 循环
    li = [11, 22, 33, 22, 44]
    for l in li:
        print(l)
    # 结果：
    #     11
    #     22
    #     33
    #     22
    #     44

# 5 in 操作
    li = [11, 22, "aa", "bb", ["a1", "b1"]]
    print(11 in li)  # True

# 6 字符串转换为列表 传给list的对象必须可以迭代
    s = "abcdef"
    li = list(s)
    print(li)  # ['a', 'b', 'c', 'd', 'e', 'f']

    # 列表转换为字符串
    li = ['a', 'b', 'c', 'd', 'e', 'f']
    print(str(li))  # ['a', 'b', 'c', 'd', 'e', 'f']
    # 直接使用字符串join方法：列表中的元素只有字符串
    print("".join(li))  # abcdef

# ================================================
    # 字符串的替换是返回一个新拷贝的对象（字符串创建后不可修改）
    s = "abcd"
    print(s.replace("a", "A"))
    # 列表里面的元素可以被替换
    li = [11,22,33,44]
    li[0] = "aa"
    print(li)  # ['aa', 22, 33, 44]
