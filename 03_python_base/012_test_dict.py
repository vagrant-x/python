if __name__ == '__main__':
    # 字典: 字典是无需的，创建字典的方式
    print({"a": 1, "b": 2})  # {'a': 1, 'b': 2}
    print(dict(a=1, b=2))  # {'a': 1, 'b': 2}
    print(dict({"a": 1, "b": 2}))  # {'a': 1, 'b': 2}
    print(dict.fromkeys(["a", "b"], 1))  # {'a': 1, 'b': 1}

# ============方法====================
#clear 清空所有的数据并返回None,
    d = {"a": 1, "b": 2, "c": 3}
    d.clear()
    print(d)  # {}

#copy 进行浅拷贝
    d = {"a": 1, "b": 2, "c": 3}
    dd = d.copy()
    print(dd)
    print("id(d) = ", id(d), ", id(dd) = ", id(dd))  # id(d) =  2191859711296 , id(dd) =  2191859711360

#fromkeys 从一个可迭代对象创建字典，并设置默认值
    print(dict.fromkeys(["a", "b"], 1))  # {'a': 1, 'b': 1}

# get 根据key 从字典中查询值，如果值不存在则返回默认值, 没有设置默认值则返回None
    d = {"a": 1, "b": 2, "c": 3}
    print(d.get("a", "0000"))  # 1
    print(d.get("d", "0000"))  # 0000
    print(d.get("d"))  # None

# items 返回字典的 k-v 元组对象的列表
    d = {"a": 1, "b": 2, "c": 3}
    print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

#keys 返回字典的所有key的列表
    d = {"a": 1, "b": 2, "c": 3}
    print(d.keys())  # dict_keys(['a', 'b', 'c'])

#pop 删除指定key的数据，并返回其值，如果没有指定默认值并且key不存在，抛KeyError
    d = {"a": 1, "b": 2, "c": 3}
    print(d.pop("a", "000000"))  # 1
    print(d.pop("d", "000000"))  # 000000
    # print(d.pop("d"))  # KeyError: 'd'
    print("----------")

# popitem 删除并返回一个（key, value） 的二元组；成对按后进先出的顺序返回；如果dict为空，则引发KeyError。
    d = {"a": 1, "b": 2, "c": 3}
    print(d.popitem())  # ('c', 3)
    print(d.popitem())  # ('b', 2)

#setdefault 设备一个值，如果key不存在，添加并设置默认值，如果key 存在，返回原来的值
    d = {"a": 1, "b": 2, "c": 3}
    print(d.setdefault("d", "0000"))  # 0000
    print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': '0000'}
    print(d.setdefault("a", "0000"))  # 1
    print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': '0000'}

# update 更新字典， 传入一个字典或可迭代对象(有k-v)
    d = {"a": 1, "b": 2, "c": 3}
    d.update({"A": 1, "B": 2})
    print(d)  # {'a': 1, 'b': 2, 'c': 3, 'A': 1, 'B': 2}
    d.update(k1=1, k2=2)
    print(d)  # {'a': 1, 'b': 2, 'c': 3, 'A': 1, 'B': 2, 'k1': 1, 'k2': 2}

#values 返回字典的值
    d = {"a": 1, "b": 2, "c": 3}
    print(d.values())  # dict_values([1, 2, 3])


#=======================================
# 字典的key 可以是数字，布尔值，字符串；int(1) 和 True 看作是相同的key
    print({"1": "1", True: "Ture"})  # {'1': '1', True: 'Ture'}
    print({1: 1, "1": "1"})  # {1: 1, '1': '1'}
    print({1: 1, "1": "1", True: "Ture"})  # {1: 'Ture', '1': '1'}

# 索引 通过索引方式获取指定的元素, 如果key不存在，抛 KeyError
    d = {"a": 1, "b": 2, "c": 3}
    print(d["a"])  # 1
    # print(d["d"])  # KeyError: 'd'
    print(d.get("a"))  # 1

#del 删除
    d = {"a": 1, "b": 2, "c": 3}
    del d["a"]
    print(d)  # {'b': 2, 'c': 3}

# for 循环
    d = {"a": 1, "b": 2, "c": 3}
    for item in d:
        print(item)
    # 结果
    #     a
    #     b
    #     c

    for item in d.keys():
        print(item)
    # 结果
    #     a
    #     b
    #     c

    for item in d.values():
        print(item)
    # 结果
    #     1
    #     2
    #     3

    for item in d.items():
        print(item)
    # 结果
    #     ('a', 1)
    #     ('b', 2)
    #     ('c', 3)

# 布尔值为 False 的情况
    print(bool(None))  # False
    print(bool(""))  # False
    print(bool(()))  # False
    print(bool([]))  # False
    print(bool({}))  # False
    print(bool(0))  # False



